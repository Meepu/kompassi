from types import SimpleNamespace
from unittest import mock

import pytest
import yaml

from core.models import Event
from dimensions.models.dimension import Dimension
from dimensions.models.dimension_value import DimensionValue
from graphql_api.schema import schema

from .excel_export import get_header_cells, get_response_cells
from .graphql.mutations.put_survey_dimension import PutSurveyDimension
from .graphql.mutations.update_response_dimensions import UpdateResponseDimensions
from .models.field import Choice, Field, FieldType
from .models.response import Response
from .models.survey import Survey
from .utils.merge_form_fields import _merge_choices, _merge_fields
from .utils.process_form_data import FieldWarning, process_form_data
from .utils.s3_presign import BUCKET_NAME, S3_ENDPOINT_URL
from .utils.summarize_responses import MatrixFieldSummary, SelectFieldSummary, TextFieldSummary, summarize_responses

# pass this as the info param to mutations to appease the graphql_check_access decorator
# (remember to also mock.patch graphql_check_access)
MOCK_INFO = SimpleNamespace(context=SimpleNamespace(user=None))


def test_process_form_data():
    fields = [
        Field.model_validate(field)
        for field in yaml.safe_load(
            """
            # single line text fields
            - type: SingleLineText
              slug: singleLineText
              title: Single line text
            - type: SingleLineText
              slug: singleLineTextRequiredMissing
              title: A required field that is missing
              required: true
            - type: SingleLineText
              slug: singleLineTextHtmlNumber
              title: A number field
              htmlType: number

            # single checkbox fields
            - type: SingleCheckbox
              slug: thisIsFalse
              title: This is false
            - type: SingleCheckbox
              slug: thisIsTrue
              title: This is true
            - type: SingleCheckbox
              slug: singleCheckboxRequiredMissing
              title: A required field that is missing
              required: true

            # single select
            - type: SingleSelect
              slug: singleSelect
              title: Single select
              choices: &choices
                - slug: choice1
                  title: Choice 1
                - slug: choice2
                  title: Choice 2
                - slug: choice3
                  title: Choice 3
            - type: SingleSelect
              slug: dropdown
              title: Dropdown
              helpText: A dropdown menu shouldn't be handled any differently
              presentation: dropdown
              choices: *choices
            - type: SingleSelect
              slug: singleSelectRequiredMissing
              title: A required field that is missing
              required: true
              choices: *choices
            - type: SingleSelect
              slug: singleSelectInvalidChoice
              title: A required field with an invalid choice selected
              choices: *choices

            # multi select fields
            - type: MultiSelect
              slug: multiSelect
              title: Multi select
              choices: *choices
            - type: MultiSelect
              slug: multiSelectNothingSelected
              title: Multi select with nothing selected
              choices: *choices
            - type: MultiSelect
              slug: multiSelectRequiredMissing
              title: A required field that is missing
              required: true
              choices: *choices

            # radio matrix fields
            - type: RadioMatrix
              slug: radioMatrix
              title: Radio matrix
              questions: &questions
                - slug: foo
                  title: Foo
                - slug: bar
                  title: Bar
              choices: *choices
            - type: RadioMatrix
              slug: radioMatrixRequiredMissing
              title: A required field that has one question missing
              required: true
              questions: *questions
              choices: *choices
            - type: RadioMatrix
              slug: radioMatrixInvalidChoice
              title: A required field with an invalid choice selected
              questions: *questions
              choices: *choices
            - type: RadioMatrix
              slug: radioMatrixInvalidQuestion
              title: A required field with an invalid question
              questions: *questions
              choices: *choices
            """
        )
    ]

    header_row = [cell for field in fields for cell in get_header_cells(field)]

    expected_header_row = [
        # single line text fields
        "singleLineText",
        "singleLineTextRequiredMissing",
        "singleLineTextHtmlNumber",
        # single checkbox fields
        "thisIsFalse",
        "thisIsTrue",
        "singleCheckboxRequiredMissing",
        # single select fields
        "singleSelect",
        "dropdown",
        "singleSelectRequiredMissing",
        "singleSelectInvalidChoice",
        # multi select fields
        "multiSelect.choice1",
        "multiSelect.choice2",
        "multiSelect.choice3",
        "multiSelectNothingSelected.choice1",
        "multiSelectNothingSelected.choice2",
        "multiSelectNothingSelected.choice3",
        "multiSelectRequiredMissing.choice1",
        "multiSelectRequiredMissing.choice2",
        "multiSelectRequiredMissing.choice3",
        # radio matrix fields
        "radioMatrix.foo",
        "radioMatrix.bar",
        "radioMatrixRequiredMissing.foo",
        "radioMatrixRequiredMissing.bar",
        "radioMatrixInvalidChoice.foo",
        "radioMatrixInvalidChoice.bar",
        "radioMatrixInvalidQuestion.foo",
        "radioMatrixInvalidQuestion.bar",
    ]

    assert header_row == expected_header_row

    form_data = {
        # single line text fields
        "singleLineText": "Hello world",
        "singleLineTextHtmlNumber": "123",
        # single checkbox fields
        "thisIsTrue": "on",
        # single select fields
        "singleSelect": "choice1",
        "dropdown": "choice2",
        "singleSelectInvalidChoice": "choice666",
        # multi select fields
        "multiSelect.choice1": "on",
        "multiSelect.choice3": "on",
        # radio matrix fields
        "radioMatrix.foo": "choice1",
        "radioMatrix.bar": "choice2",
        "radioMatrixRequiredMissing.foo": "choice3",
        "radioMatrixInvalidChoice.foo": "choice666",
        "radioMatrixInvalidChoice.bar": "choice1",
        "radioMatrixInvalidQuestion.foo": "choice2",
        "radioMatrixInvalidQuestion.notFoo": "choice1",
        "radioMatrixInvalidQuestion.bar": "choice2",
    }

    expected_values = dict(
        # single line text fields
        singleLineText="Hello world",
        singleLineTextRequiredMissing="",
        singleLineTextHtmlNumber=123,
        # single checkbox fields
        thisIsTrue=True,
        thisIsFalse=False,
        # single select fields
        singleSelect="choice1",
        dropdown="choice2",
        singleSelectInvalidChoice="choice666",  # NOTE! See comment in forms/utils.py:process_form_data
        singleCheckboxRequiredMissing=False,
        singleSelectRequiredMissing="",
        # multi select fields
        multiSelect=["choice1", "choice3"],
        multiSelectNothingSelected=[],
        multiSelectRequiredMissing=[],
        # radio matrix fields
        radioMatrix={
            "foo": "choice1",
            "bar": "choice2",
        },
        radioMatrixRequiredMissing={
            "foo": "choice3",
        },
        radioMatrixInvalidChoice={
            "foo": "choice666",
            "bar": "choice1",
        },
        radioMatrixInvalidQuestion={
            "foo": "choice2",
            "notFoo": "choice1",
            "bar": "choice2",
        },
    )

    expected_warnings = dict(
        # single line text fields
        singleLineTextRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        # single checkbox fields
        singleCheckboxRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        # single select fields
        singleSelectRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        singleSelectInvalidChoice=[FieldWarning.INVALID_CHOICE],
        # multi select fields
        multiSelectRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        # radio matrix fields
        radioMatrixRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        radioMatrixInvalidChoice=[FieldWarning.INVALID_CHOICE],
        radioMatrixInvalidQuestion=[FieldWarning.INVALID_CHOICE],
    )

    values, warnings = process_form_data(fields, form_data)

    assert values == expected_values
    assert warnings == expected_warnings

    expected_response_row = [
        # singleLineText
        "Hello world",
        # singleLineTextRequiredMissing
        "",
        # singleLineTextHtmlNumber
        123,
        # thisIsFalse
        False,
        # thisIsTrue
        True,
        # singleCheckboxRequiredMissing
        False,
        # singleSelect
        "choice1",
        # dropdown
        "choice2",
        # singleSelectRequiredMissing
        "",
        # singleSelectInvalidChoice
        "choice666",
        # multiSelect.choice1
        True,
        # multiSelect.choice2
        False,
        # multiSelect.choice3
        True,
        # multiSelectNothingSelected.choice1
        False,
        # multiSelectNothingSelected.choice2
        False,
        # multiSelectNothingSelected.choice3
        False,
        # multiSelectRequiredMissing.choice1
        False,
        # multiSelectRequiredMissing.choice2
        False,
        # multiSelectRequiredMissing.choice3
        False,
        # radioMatrix.foo
        "choice1",
        # radioMatrix.bar
        "choice2",
        # radioMatrixRequiredMissing.foo
        "choice3",
        # radioMatrixRequiredMissing.bar
        "",
        # radioMatrixInvalidChoice.foo
        "choice666",
        # radioMatrixInvalidChoice.bar
        "choice1",
        # radioMatrixInvalidQuestion.foo
        "choice2",
        # radioMatrixInvalidQuestion.bar
        "choice2",
    ]

    response_row = [cell for field in fields for cell in get_response_cells(field, values)]
    assert response_row == expected_response_row


def test_process_form_data_file_upload():
    """
    Presigning S3 URLs is an offline operation, so we can test it without mocking
    """
    fields = [
        Field(slug="fileUpload", type=FieldType.FILE_UPLOAD),
        Field(slug="multiFileUpload", type=FieldType.FILE_UPLOAD, multiple=True),
        Field(slug="fileUploadRequiredMissing", type=FieldType.FILE_UPLOAD, required=True),
        Field(slug="fileUploadInvalidUrl", type=FieldType.FILE_UPLOAD),
        Field(slug="fileUploadBogusValue", type=FieldType.FILE_UPLOAD),
    ]

    # for file upload, the form data item is a list of S3 URLs
    form_data = {
        "fileUpload": [f"{S3_ENDPOINT_URL}/{BUCKET_NAME}/file1.txt"],
        "multiFileUpload": [
            f"{S3_ENDPOINT_URL}/{BUCKET_NAME}/file2.txt",
            f"{S3_ENDPOINT_URL}/{BUCKET_NAME}/file3.txt",
        ],
        "fileUploadInvalidUrl": ["https://example.com/file.txt"],
        "fileUploadBogusValue": "not a list",
    }

    expected_warnings = dict(
        fileUploadRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        fileUploadInvalidUrl=[FieldWarning.INVALID_VALUE],
        fileUploadBogusValue=[FieldWarning.INVALID_VALUE],
    )

    values, warnings = process_form_data(fields, form_data)
    assert warnings == expected_warnings

    def is_valid_presigned_url(url: str):
        return url.startswith(f"{S3_ENDPOINT_URL}/{BUCKET_NAME}/") and "?" in url

    assert all(is_valid_presigned_url(url) for url in values["fileUpload"])
    assert all(is_valid_presigned_url(url) for url in values["multiFileUpload"])
    assert "fileUploadRequiredMissing" not in values
    assert "fileUploadInvalidUrl" not in values


def test_process_form_data_number_field():
    fields = [
        Field(slug="numberField", type=FieldType.NUMBER_FIELD),
        Field(slug="numberFieldRequiredMissing", type=FieldType.NUMBER_FIELD, required=True),
        Field(slug="numberFieldInvalidValue", type=FieldType.NUMBER_FIELD),
        Field(slug="numberFieldWithDecimalPlaces", type=FieldType.NUMBER_FIELD, decimalPlaces=2),
    ]

    form_data = {
        "numberField": "123",
        "numberFieldInvalidValue": "not a number",
        "numberFieldWithDecimalPlaces": "1.23",
    }

    expected_values = dict(
        numberField=123,
        numberFieldWithDecimalPlaces=1.23,
    )

    expected_warnings = dict(
        numberFieldRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        numberFieldInvalidValue=[FieldWarning.INVALID_VALUE],
    )

    values, warnings = process_form_data(fields, form_data)
    assert values == expected_values
    assert warnings == expected_warnings


def test_process_form_data_decimal_field():
    fields = [
        Field(slug="decimalField", type=FieldType.DECIMAL_FIELD),
        Field(slug="decimalFieldWithDecimalPlaces", type=FieldType.DECIMAL_FIELD, decimalPlaces=2),
        Field(slug="decimalFieldRequiredMissing", type=FieldType.DECIMAL_FIELD, required=True),
        Field(slug="decimalFieldInvalidValue", type=FieldType.DECIMAL_FIELD),
        Field(slug="decimalWithDifferingDecimalPlaces1", type=FieldType.DECIMAL_FIELD, decimalPlaces=2),
        Field(slug="decimalWithDifferingDecimalPlaces2", type=FieldType.DECIMAL_FIELD, decimalPlaces=2),
    ]

    form_data = {
        "decimalField": "123",
        "decimalFieldWithDecimalPlaces": "1.23",
        "decimalFieldInvalidValue": "not a number",
        "decimalWithDifferingDecimalPlaces1": "4",
        "decimalWithDifferingDecimalPlaces2": "3.4324",
    }

    expected_values = dict(
        decimalField="123",
        decimalFieldWithDecimalPlaces="1.23",
        decimalWithDifferingDecimalPlaces1="4.00",
        decimalWithDifferingDecimalPlaces2="3.43",
    )

    expected_warnings = dict(
        decimalFieldRequiredMissing=[FieldWarning.REQUIRED_MISSING],
        decimalFieldInvalidValue=[FieldWarning.INVALID_VALUE],
    )

    values, warnings = process_form_data(fields, form_data)
    assert values == expected_values
    assert warnings == expected_warnings


def test_merge_choices():
    lhs_choices = [
        Choice(slug="foo", title="Foo"),
        Choice(slug="bar", title="Bar"),
        Choice(slug="quux", title="Quux"),
    ]

    rhs_choices = [
        Choice(slug="bar", title="Bar"),
        Choice(slug="baz", title="Baz"),
    ]

    expected_merged_choices = [
        Choice(slug="foo", title="Foo"),
        Choice(slug="bar", title="Bar"),
        Choice(slug="quux", title="Quux"),
        Choice(slug="baz", title="Baz"),
    ]

    assert _merge_choices(lhs_choices, rhs_choices) == expected_merged_choices


def test_merge_fields():
    lhs_fields = [
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInBoth",
        ),
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInLhs",
        ),
    ]

    rhs_fields = [
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInBoth",
        ),
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInRhs",
        ),
    ]

    expected_merged_fields = [
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInBoth",
        ),
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInLhs",
        ),
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="presentInRhs",
        ),
    ]

    assert _merge_fields(lhs_fields, rhs_fields) == expected_merged_fields


def test_summarize_responses():
    choices = [
        Choice(slug="choice1", title="Choice 1"),
        Choice(slug="choice2", title="Choice 2"),
        Choice(slug="choice3", title="Choice 3"),
    ]

    fields = [
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            slug="singleLineText",
        ),
        Field(
            type=FieldType.SINGLE_LINE_TEXT,
            htmlType="number",
            slug="numberField",
        ),
        Field(
            type=FieldType.DIVIDER,
            slug="dividerShouldNotBePresentInSummary",
        ),
        Field(
            type=FieldType.SINGLE_SELECT,
            slug="singleSelect",
            choices=choices,
        ),
        Field(
            type=FieldType.MULTI_SELECT,
            slug="multiSelect",
            choices=choices,
        ),
        Field(
            type=FieldType.RADIO_MATRIX,
            slug="radioMatrix",
            questions=[
                Choice(
                    slug="foo",
                    title="Foo",
                ),
                Choice(
                    slug="bar",
                    title="Bar",
                ),
            ],
            choices=choices,
        ),
    ]

    responses = [
        {
            "singleLineText": "Hello world",
            "numberField": 5,
            "singleSelect": "choice1",
            "multiSelect": ["choice1", "choice3"],
            "radioMatrix": {
                "foo": "choice1",
                "bar": "choice2",
            },
        },
        {
            "singleLineText": "Hello world",
            "numberField": 6,
            "singleSelect": "choice2",
            "multiSelect": [],
            "radioMatrix": {
                "foo": "choice2",
                "bar": "choice2",
            },
        },
        # surprise choice that is not included in choices!
        # an admin may have removed it from the form after the response was submitted
        {
            "singleSelect": "choice666",
            "multiSelect": ["choice666"],
            "radioMatrix": {
                "foo": "choice666",
                # did not answer this question
                # "bar": "choice666",
            },
        },
    ]

    expected_summary = {
        "singleLineText": TextFieldSummary(
            countResponses=2,
            countMissingResponses=1,
            summary=["Hello world", "Hello world"],
        ),
        "numberField": SelectFieldSummary(
            countResponses=2,
            countMissingResponses=1,
            summary={"5": 1, "6": 1},
        ),
        "singleSelect": SelectFieldSummary(
            countResponses=3,
            countMissingResponses=0,
            summary={"choice1": 1, "choice2": 1, "choice3": 0, "choice666": 1},
        ),
        "multiSelect": SelectFieldSummary(
            countResponses=2,
            countMissingResponses=1,
            summary={"choice1": 1, "choice2": 0, "choice3": 1, "choice666": 1},
        ),
        "radioMatrix": MatrixFieldSummary(
            countResponses=3,
            countMissingResponses=0,
            summary={
                "foo": {"choice1": 1, "choice2": 1, "choice3": 0, "choice666": 1},
                "bar": {"choice1": 0, "choice2": 2, "choice3": 0},
            },
        ),
    }

    assert summarize_responses(fields, responses) == expected_summary


@pytest.mark.django_db
@mock.patch("forms.graphql.mutations.update_response_dimensions.graphql_check_instance", autospec=True)
def test_lift_and_set_dimensions(_patched_graphql_check_instance):
    event, _created = Event.get_or_create_dummy()

    survey = Survey.objects.create(
        event=event,
        slug="test-survey",
    )

    dimension = Dimension.objects.create(
        universe=survey.universe,
        slug="test-dimension",
    )

    DimensionValue.objects.bulk_create(
        [
            DimensionValue(
                dimension=dimension,
                slug="test-dimension-value-1",
            ),
            DimensionValue(
                dimension=dimension,
                slug="test-dimension-value-2",
            ),
        ]
    )

    dimension2 = Dimension.objects.create(
        universe=survey.universe,
        slug="test-dimension2",
        title_en="Test dimension 2",
    )

    DimensionValue.objects.bulk_create(
        [
            DimensionValue(
                dimension=dimension2,
                slug="test-dimension2-value-1",
            ),
            DimensionValue(
                dimension=dimension2,
                slug="test-dimension2-value-2",
            ),
        ]
    )

    form = survey.languages.create(
        event=event,
        slug="test-survey-en",
        language="en",
        fields=[
            dict(
                slug="test-dimension",
                type="SingleSelect",
                choicesFrom=dict(dimension="test-dimension"),
            )
        ],
    )

    response = Response.objects.create(
        form=form,
        form_data={"test-dimension": "test-dimension-value-1"},
    )

    response.lift_dimension_values()
    response.refresh_from_db()

    assert response.cached_dimensions == {
        "test-dimension": ["test-dimension-value-1"],
    }

    # also tests set_dimension_values
    # XXX: Graphene does some deep magic that causes using UpdateResponseDimensionsInput
    # as a value type to fail, so we have to use SimpleNamespace instead
    UpdateResponseDimensions.mutate(
        None,
        MOCK_INFO,
        SimpleNamespace(
            event_slug=event.slug,
            survey_slug=survey.slug,
            response_id=response.id,
            form_data={
                # SingleSelect used as dimension field
                "test-dimension": "test-dimension-value-2",
                # MultiSelect used as dimension field
                "test-dimension2.test-dimension2-value-1": "checked",
                "test-dimension2.test-dimension2-value-2": "checked",
            },
        ),  # type: ignore
    )

    response.refresh_from_db()

    assert response.cached_dimensions == {
        "test-dimension": ["test-dimension-value-2"],
        "test-dimension2": ["test-dimension2-value-1", "test-dimension2-value-2"],
    }


@pytest.mark.django_db
@mock.patch("forms.graphql.mutations.put_survey_dimension.graphql_check_instance", autospec=True)
def test_put_survey_dimension(_patched_graphql_check_instance):
    form_data = {
        "slug": "test-dimension",
        "title.en": "Test dimension",
        "title.sv": "Testdimension",
        "isKeyDimension": "on",
    }

    event, _created = Event.get_or_create_dummy()

    survey = Survey.objects.create(
        event=event,
        slug="test-survey",
    )

    PutSurveyDimension.mutate(
        None,
        MOCK_INFO,
        SimpleNamespace(
            event_slug=event.slug,
            survey_slug=survey.slug,
            form_data=form_data,
            dimension_slug=None,
        ),  # type: ignore
    )

    dimension = Dimension.objects.get(universe=survey.universe, slug="test-dimension")

    assert dimension.slug == "test-dimension"
    assert dimension.title_en == "Test dimension"
    assert dimension.title_sv == "Testdimension"
    assert dimension.title_fi == ""
    assert dimension.is_key_dimension is True
    assert dimension.is_multi_value is False


@pytest.mark.django_db
@mock.patch("forms.graphql.meta.graphql_check_instance", autospec=True)
def test_survey_without_forms(_patched_graphql_check_instance):
    """
    A survey that doesn't yet have any Forms should degrade gracefully.
    """
    event, _created = Event.get_or_create_dummy()

    Survey.objects.create(
        event=event,
        slug="test-survey",
    )

    result = schema.execute(
        """
          query SurveyWithoutForms {
            event(slug: "dummy-event") {
              forms {
                survey(slug: "test-survey") {
                  title(lang: "fi")
                }
              }
            }
          }
        """,
        None,
        MOCK_INFO,
    )

    assert not result.errors
