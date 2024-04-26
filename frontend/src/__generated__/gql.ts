/* eslint-disable */
import * as types from './graphql';
import { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';

/**
 * Map of all GraphQL operations in the project.
 *
 * This map has several performance disadvantages:
 * 1. It is not tree-shakeable, so it will include all operations in the project.
 * 2. It is not minifiable, so the string of a GraphQL query will be multiple times inside the bundle.
 * 3. It does not support dead code elimination, so it will add unused operations.
 *
 * Therefore it is highly recommended to use the babel or swc plugin for production.
 */
const documents = {
    "\n  mutation MarkProgramAsFavorite($input: FavoriteInput!) {\n    markProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n": types.MarkProgramAsFavoriteDocument,
    "\n  mutation UnmarkProgramAsFavorite($input: FavoriteInput!) {\n    unmarkProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n": types.UnmarkProgramAsFavoriteDocument,
    "\n  fragment ProgramList on ProgramType {\n    slug\n    title\n    cachedDimensions\n    scheduleItems {\n      startTime\n      endTime\n    }\n  }\n": types.ProgramListFragmentDoc,
    "\n  query ProgramListQuery(\n    $locale: String\n    $eventSlug: String!\n    $filters: [DimensionFilterInput!]\n    $hidePast: Boolean\n  ) {\n    profile {\n      program {\n        programs(\n          eventSlug: $eventSlug\n          filters: $filters\n          hidePast: $hidePast\n        ) {\n          ...ProgramList\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        calendarExportLink\n\n        dimensions {\n          slug\n          title(lang: $locale)\n\n          values {\n            slug\n            title(lang: $locale)\n          }\n        }\n\n        locationDimension {\n          slug\n        }\n\n        programs(filters: $filters, hidePast: $hidePast) {\n          ...ProgramList\n        }\n      }\n    }\n  }\n": types.ProgramListQueryDocument,
    "\n  query ProgramDetailQuery(\n    $eventSlug: String!\n    $programSlug: String!\n    $locale: String\n  ) {\n    profile {\n      program {\n        programs(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      program {\n        calendarExportLink\n        program(slug: $programSlug) {\n          title\n          description\n          cachedHosts\n\n          links(lang: $locale) {\n            type\n            href\n            title\n          }\n\n          dimensions {\n            dimension {\n              slug\n              title(lang: $locale)\n            }\n            value {\n              slug\n              title(lang: $locale)\n            }\n          }\n          scheduleItems {\n            startTime\n            endTime\n          }\n        }\n      }\n    }\n  }\n": types.ProgramDetailQueryDocument,
    "\n  query NewProgramQuery(\n    $eventSlug: String!\n    $formSlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      program {\n        skipOfferFormSelection\n\n        offerForm(slug: $formSlug) {\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n": types.NewProgramQueryDocument,
    "\n  query NewProgramFormSelectionQuery($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        skipOfferFormSelection\n\n        offerForms {\n          slug\n          shortDescription(lang: $locale)\n          form(lang: $locale) {\n            title\n            slug\n          }\n        }\n      }\n    }\n  }\n": types.NewProgramFormSelectionQueryDocument,
    "\n  mutation CreateSurveyResponse($input: CreateSurveyResponseInput!) {\n    createSurveyResponse(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n": types.CreateSurveyResponseDocument,
    "\n  mutation InitFileUploadMutation($input: InitFileUploadInput!) {\n    initFileUpload(input: $input) {\n      uploadUrl\n      fileUrl\n    }\n  }\n": types.InitFileUploadMutationDocument,
    "\n  mutation PutSurveyDimension($input: PutSurveyDimensionInput!) {\n    putSurveyDimension(input: $input) {\n      dimension {\n        slug\n      }\n    }\n  }\n": types.PutSurveyDimensionDocument,
    "\n  mutation DeleteSurveyDimension($input: DeleteSurveyDimensionInput!) {\n    deleteSurveyDimension(input: $input) {\n      slug\n    }\n  }\n": types.DeleteSurveyDimensionDocument,
    "\n  mutation PutSurveyDimensionValue($input: PutSurveyDimensionValueInput!) {\n    putSurveyDimensionValue(input: $input) {\n      value {\n        slug\n      }\n    }\n  }\n": types.PutSurveyDimensionValueDocument,
    "\n  mutation DeleteSurveyDimensionValue(\n    $input: DeleteSurveyDimensionValueInput!\n  ) {\n    deleteSurveyDimensionValue(input: $input) {\n      slug\n    }\n  }\n": types.DeleteSurveyDimensionValueDocument,
    "\n  fragment ValueFields on SurveyDimensionValueType {\n    slug\n    color\n    canRemove\n    title(lang: $locale)\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n  }\n": types.ValueFieldsFragmentDoc,
    "\n  fragment DimensionRowGroup on SurveyDimensionType {\n    slug\n    canRemove\n    title(lang: $locale)\n    isKeyDimension\n    isMultiValue\n    isShownToRespondent\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n    values {\n      ...ValueFields\n    }\n  }\n": types.DimensionRowGroupFragmentDoc,
    "\n  query DimensionsList(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String!\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          slug\n          title(lang: $locale)\n          canRemove\n          languages {\n            language\n          }\n          dimensions {\n            ...DimensionRowGroup\n          }\n        }\n      }\n    }\n  }\n": types.DimensionsListDocument,
    "\n  mutation UpdateSurveyLanguageMutation($input: UpdateSurveyLanguageInput!) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n": types.UpdateSurveyLanguageMutationDocument,
    "\n  mutation DeleteSurveyLanguage($input: DeleteSurveyLanguageInput!) {\n    deleteSurveyLanguage(input: $input) {\n      language\n    }\n  }\n": types.DeleteSurveyLanguageDocument,
    "\n  mutation UpdateSurveyFieldsLanguageMutation(\n    $input: UpdateSurveyLanguageInput!\n  ) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n": types.UpdateSurveyFieldsLanguageMutationDocument,
    "\n  fragment EditSurveyFieldsPage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      fields(enrich: false)\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n": types.EditSurveyFieldsPageFragmentDoc,
    "\n  query EditSurveyFieldsPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyFieldsPage\n        }\n      }\n    }\n  }\n": types.EditSurveyFieldsPageQueryDocument,
    "\n  fragment EditSurveyLanguagePage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      description\n      thankYouMessage\n      fields\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n": types.EditSurveyLanguagePageFragmentDoc,
    "\n  query EditSurveyLanguagePageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyLanguagePage\n        }\n      }\n    }\n  }\n": types.EditSurveyLanguagePageQueryDocument,
    "\n  mutation CreateSurveyLanguage($input: CreateSurveyLanguageInput!) {\n    createSurveyLanguage(input: $input) {\n      form {\n        language\n      }\n    }\n  }\n": types.CreateSurveyLanguageDocument,
    "\n  mutation UpdateSurveyMutation($input: UpdateSurveyInput!) {\n    updateSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n": types.UpdateSurveyMutationDocument,
    "\n  mutation DeleteSurveyMutation($input: DeleteSurveyInput!) {\n    deleteSurvey(input: $input) {\n      slug\n    }\n  }\n": types.DeleteSurveyMutationDocument,
    "\n  fragment EditSurveyPage on SurveyType {\n    slug\n    title(lang: $locale)\n    loginRequired\n    anonymity\n    maxResponsesPerUser\n    countResponsesByCurrentUser\n    activeFrom\n    activeUntil\n    canRemove\n\n    languages {\n      title\n      language\n      canRemove\n    }\n  }\n": types.EditSurveyPageFragmentDoc,
    "\n  query EditSurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyPage\n        }\n      }\n    }\n  }\n": types.EditSurveyPageQueryDocument,
    "\n  query SurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          loginRequired\n          anonymity\n          maxResponsesPerUser\n          countResponsesByCurrentUser\n\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n": types.SurveyPageQueryDocument,
    "\n  mutation UpdateResponseDimensions($input: UpdateResponseDimensionsInput!) {\n    updateResponseDimensions(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n": types.UpdateResponseDimensionsDocument,
    "\n  query SurveyResponseDetail(\n    $eventSlug: String!\n    $surveySlug: String!\n    $responseId: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          slug\n          anonymity\n          dimensions {\n            title(lang: $locale)\n            slug\n            isMultiValue\n            values {\n              title(lang: $locale)\n              slug\n              color\n            }\n          }\n          response(id: $responseId) {\n            id\n            sequenceNumber\n            createdAt\n            createdBy {\n              displayName\n              email\n            }\n            language\n            values\n            form {\n              fields\n              layout\n            }\n            cachedDimensions\n          }\n        }\n      }\n    }\n  }\n": types.SurveyResponseDetailDocument,
    "\n  mutation SubscribeToSurveyResponses($input: SubscriptionInput!) {\n    subscribeToSurveyResponses(input: $input) {\n      success\n    }\n  }\n": types.SubscribeToSurveyResponsesDocument,
    "\n  mutation UnsubscribeFromSurveyResponses($input: SubscriptionInput!) {\n    unsubscribeFromSurveyResponses(input: $input) {\n      success\n    }\n  }\n": types.UnsubscribeFromSurveyResponsesDocument,
    "\n  fragment SurveyResponse on LimitedResponseType {\n    id\n    sequenceNumber\n    createdAt\n    createdBy {\n      displayName\n    }\n    language\n    values(keyFieldsOnly: true)\n    cachedDimensions(keyDimensionsOnly: true)\n  }\n": types.SurveyResponseFragmentDoc,
    "\n  query FormResponses(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    profile {\n      forms {\n        surveys(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          anonymity\n\n          fields(lang: $locale, keyFieldsOnly: true)\n          dimensions {\n            slug\n            title(lang: $locale)\n            isKeyDimension\n\n            values {\n              slug\n              title(lang: $locale)\n              color\n            }\n          }\n\n          countResponses\n\n          responses(filters: $filters) {\n            ...SurveyResponse\n          }\n        }\n      }\n    }\n  }\n": types.FormResponsesDocument,
    "\n  query SurveySummary(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          fields(lang: $locale)\n          summary(filters: $filters)\n          countFilteredResponses: countResponses(filters: $filters)\n          countResponses\n          dimensions {\n            slug\n            title(lang: $locale)\n            values {\n              slug\n              title(lang: $locale)\n            }\n          }\n        }\n      }\n    }\n  }\n": types.SurveySummaryDocument,
    "\n  query SurveyThankYouPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          form(lang: $locale) {\n            title\n            thankYouMessage\n          }\n        }\n      }\n    }\n  }\n": types.SurveyThankYouPageQueryDocument,
    "\n  mutation CreateSurvey($input: CreateSurveyInput!) {\n    createSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n": types.CreateSurveyDocument,
    "\n  fragment Survey on SurveyType {\n    slug\n    title(lang: $locale)\n    isActive\n    activeFrom\n    activeUntil\n    countResponses\n\n    languages {\n      language\n    }\n  }\n": types.SurveyFragmentDoc,
    "\n  query Surveys($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        surveys(includeInactive: true) {\n          ...Survey\n        }\n      }\n    }\n  }\n": types.SurveysDocument,
    "\n  query ProfileSurveyResponsePage($locale: String!, $responseId: String!) {\n    profile {\n      forms {\n        response(id: $responseId) {\n          id\n          createdAt\n          values\n\n          dimensions {\n            ...DimensionBadge\n          }\n\n          form {\n            slug\n            title\n            language\n            fields\n            layout\n            event {\n              slug\n              name\n            }\n            survey {\n              anonymity\n            }\n          }\n        }\n      }\n    }\n  }\n": types.ProfileSurveyResponsePageDocument,
    "\n  fragment ProfileResponsesTableRow on ProfileResponseType {\n    id\n    createdAt\n    dimensions(keyDimensionsOnly: true) {\n      dimension {\n        slug\n        title(lang: $locale)\n      }\n\n      value {\n        slug\n        title(lang: $locale)\n        color\n      }\n    }\n    form {\n      slug\n      title\n      event {\n        slug\n        name\n      }\n    }\n  }\n": types.ProfileResponsesTableRowFragmentDoc,
    "\n  query OwnFormResponses($locale: String!) {\n    profile {\n      forms {\n        responses {\n          ...ProfileResponsesTableRow\n        }\n      }\n    }\n  }\n": types.OwnFormResponsesDocument,
    "\n  fragment DimensionBadge on ResponseDimensionValueType {\n    dimension {\n      slug\n      title(lang: $locale)\n    }\n\n    value {\n      slug\n      title(lang: $locale)\n      color\n    }\n  }\n": types.DimensionBadgeFragmentDoc,
};

/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 *
 *
 * @example
 * ```ts
 * const query = graphql(`query GetUser($id: ID!) { user(id: $id) { name } }`);
 * ```
 *
 * The query argument is unknown!
 * Please regenerate the types.
 */
export function graphql(source: string): unknown;

/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation MarkProgramAsFavorite($input: FavoriteInput!) {\n    markProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n"): (typeof documents)["\n  mutation MarkProgramAsFavorite($input: FavoriteInput!) {\n    markProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UnmarkProgramAsFavorite($input: FavoriteInput!) {\n    unmarkProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n"): (typeof documents)["\n  mutation UnmarkProgramAsFavorite($input: FavoriteInput!) {\n    unmarkProgramAsFavorite(input: $input) {\n      success\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment ProgramList on ProgramType {\n    slug\n    title\n    cachedDimensions\n    scheduleItems {\n      startTime\n      endTime\n    }\n  }\n"): (typeof documents)["\n  fragment ProgramList on ProgramType {\n    slug\n    title\n    cachedDimensions\n    scheduleItems {\n      startTime\n      endTime\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query ProgramListQuery(\n    $locale: String\n    $eventSlug: String!\n    $filters: [DimensionFilterInput!]\n    $hidePast: Boolean\n  ) {\n    profile {\n      program {\n        programs(\n          eventSlug: $eventSlug\n          filters: $filters\n          hidePast: $hidePast\n        ) {\n          ...ProgramList\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        calendarExportLink\n\n        dimensions {\n          slug\n          title(lang: $locale)\n\n          values {\n            slug\n            title(lang: $locale)\n          }\n        }\n\n        locationDimension {\n          slug\n        }\n\n        programs(filters: $filters, hidePast: $hidePast) {\n          ...ProgramList\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query ProgramListQuery(\n    $locale: String\n    $eventSlug: String!\n    $filters: [DimensionFilterInput!]\n    $hidePast: Boolean\n  ) {\n    profile {\n      program {\n        programs(\n          eventSlug: $eventSlug\n          filters: $filters\n          hidePast: $hidePast\n        ) {\n          ...ProgramList\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        calendarExportLink\n\n        dimensions {\n          slug\n          title(lang: $locale)\n\n          values {\n            slug\n            title(lang: $locale)\n          }\n        }\n\n        locationDimension {\n          slug\n        }\n\n        programs(filters: $filters, hidePast: $hidePast) {\n          ...ProgramList\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query ProgramDetailQuery(\n    $eventSlug: String!\n    $programSlug: String!\n    $locale: String\n  ) {\n    profile {\n      program {\n        programs(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      program {\n        calendarExportLink\n        program(slug: $programSlug) {\n          title\n          description\n          cachedHosts\n\n          links(lang: $locale) {\n            type\n            href\n            title\n          }\n\n          dimensions {\n            dimension {\n              slug\n              title(lang: $locale)\n            }\n            value {\n              slug\n              title(lang: $locale)\n            }\n          }\n          scheduleItems {\n            startTime\n            endTime\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query ProgramDetailQuery(\n    $eventSlug: String!\n    $programSlug: String!\n    $locale: String\n  ) {\n    profile {\n      program {\n        programs(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n\n    event(slug: $eventSlug) {\n      name\n      program {\n        calendarExportLink\n        program(slug: $programSlug) {\n          title\n          description\n          cachedHosts\n\n          links(lang: $locale) {\n            type\n            href\n            title\n          }\n\n          dimensions {\n            dimension {\n              slug\n              title(lang: $locale)\n            }\n            value {\n              slug\n              title(lang: $locale)\n            }\n          }\n          scheduleItems {\n            startTime\n            endTime\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query NewProgramQuery(\n    $eventSlug: String!\n    $formSlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      program {\n        skipOfferFormSelection\n\n        offerForm(slug: $formSlug) {\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query NewProgramQuery(\n    $eventSlug: String!\n    $formSlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      program {\n        skipOfferFormSelection\n\n        offerForm(slug: $formSlug) {\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query NewProgramFormSelectionQuery($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        skipOfferFormSelection\n\n        offerForms {\n          slug\n          shortDescription(lang: $locale)\n          form(lang: $locale) {\n            title\n            slug\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query NewProgramFormSelectionQuery($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n      slug\n\n      program {\n        skipOfferFormSelection\n\n        offerForms {\n          slug\n          shortDescription(lang: $locale)\n          form(lang: $locale) {\n            title\n            slug\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation CreateSurveyResponse($input: CreateSurveyResponseInput!) {\n    createSurveyResponse(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation CreateSurveyResponse($input: CreateSurveyResponseInput!) {\n    createSurveyResponse(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation InitFileUploadMutation($input: InitFileUploadInput!) {\n    initFileUpload(input: $input) {\n      uploadUrl\n      fileUrl\n    }\n  }\n"): (typeof documents)["\n  mutation InitFileUploadMutation($input: InitFileUploadInput!) {\n    initFileUpload(input: $input) {\n      uploadUrl\n      fileUrl\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation PutSurveyDimension($input: PutSurveyDimensionInput!) {\n    putSurveyDimension(input: $input) {\n      dimension {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation PutSurveyDimension($input: PutSurveyDimensionInput!) {\n    putSurveyDimension(input: $input) {\n      dimension {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation DeleteSurveyDimension($input: DeleteSurveyDimensionInput!) {\n    deleteSurveyDimension(input: $input) {\n      slug\n    }\n  }\n"): (typeof documents)["\n  mutation DeleteSurveyDimension($input: DeleteSurveyDimensionInput!) {\n    deleteSurveyDimension(input: $input) {\n      slug\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation PutSurveyDimensionValue($input: PutSurveyDimensionValueInput!) {\n    putSurveyDimensionValue(input: $input) {\n      value {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation PutSurveyDimensionValue($input: PutSurveyDimensionValueInput!) {\n    putSurveyDimensionValue(input: $input) {\n      value {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation DeleteSurveyDimensionValue(\n    $input: DeleteSurveyDimensionValueInput!\n  ) {\n    deleteSurveyDimensionValue(input: $input) {\n      slug\n    }\n  }\n"): (typeof documents)["\n  mutation DeleteSurveyDimensionValue(\n    $input: DeleteSurveyDimensionValueInput!\n  ) {\n    deleteSurveyDimensionValue(input: $input) {\n      slug\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment ValueFields on SurveyDimensionValueType {\n    slug\n    color\n    canRemove\n    title(lang: $locale)\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n  }\n"): (typeof documents)["\n  fragment ValueFields on SurveyDimensionValueType {\n    slug\n    color\n    canRemove\n    title(lang: $locale)\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment DimensionRowGroup on SurveyDimensionType {\n    slug\n    canRemove\n    title(lang: $locale)\n    isKeyDimension\n    isMultiValue\n    isShownToRespondent\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n    values {\n      ...ValueFields\n    }\n  }\n"): (typeof documents)["\n  fragment DimensionRowGroup on SurveyDimensionType {\n    slug\n    canRemove\n    title(lang: $locale)\n    isKeyDimension\n    isMultiValue\n    isShownToRespondent\n    titleFi: title(lang: \"fi\")\n    titleEn: title(lang: \"en\")\n    titleSv: title(lang: \"sv\")\n    values {\n      ...ValueFields\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query DimensionsList(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String!\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          slug\n          title(lang: $locale)\n          canRemove\n          languages {\n            language\n          }\n          dimensions {\n            ...DimensionRowGroup\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query DimensionsList(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String!\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          slug\n          title(lang: $locale)\n          canRemove\n          languages {\n            language\n          }\n          dimensions {\n            ...DimensionRowGroup\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UpdateSurveyLanguageMutation($input: UpdateSurveyLanguageInput!) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation UpdateSurveyLanguageMutation($input: UpdateSurveyLanguageInput!) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation DeleteSurveyLanguage($input: DeleteSurveyLanguageInput!) {\n    deleteSurveyLanguage(input: $input) {\n      language\n    }\n  }\n"): (typeof documents)["\n  mutation DeleteSurveyLanguage($input: DeleteSurveyLanguageInput!) {\n    deleteSurveyLanguage(input: $input) {\n      language\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UpdateSurveyFieldsLanguageMutation(\n    $input: UpdateSurveyLanguageInput!\n  ) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation UpdateSurveyFieldsLanguageMutation(\n    $input: UpdateSurveyLanguageInput!\n  ) {\n    updateSurveyLanguage(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment EditSurveyFieldsPage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      fields(enrich: false)\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n"): (typeof documents)["\n  fragment EditSurveyFieldsPage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      fields(enrich: false)\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query EditSurveyFieldsPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyFieldsPage\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query EditSurveyFieldsPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyFieldsPage\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment EditSurveyLanguagePage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      description\n      thankYouMessage\n      fields\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n"): (typeof documents)["\n  fragment EditSurveyLanguagePage on SurveyType {\n    slug\n    title(lang: $locale)\n    canRemove\n\n    form(lang: $language) {\n      title\n      language\n      description\n      thankYouMessage\n      fields\n      canRemove\n    }\n\n    languages {\n      language\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query EditSurveyLanguagePageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyLanguagePage\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query EditSurveyLanguagePageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $language: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyLanguagePage\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation CreateSurveyLanguage($input: CreateSurveyLanguageInput!) {\n    createSurveyLanguage(input: $input) {\n      form {\n        language\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation CreateSurveyLanguage($input: CreateSurveyLanguageInput!) {\n    createSurveyLanguage(input: $input) {\n      form {\n        language\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UpdateSurveyMutation($input: UpdateSurveyInput!) {\n    updateSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation UpdateSurveyMutation($input: UpdateSurveyInput!) {\n    updateSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation DeleteSurveyMutation($input: DeleteSurveyInput!) {\n    deleteSurvey(input: $input) {\n      slug\n    }\n  }\n"): (typeof documents)["\n  mutation DeleteSurveyMutation($input: DeleteSurveyInput!) {\n    deleteSurvey(input: $input) {\n      slug\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment EditSurveyPage on SurveyType {\n    slug\n    title(lang: $locale)\n    loginRequired\n    anonymity\n    maxResponsesPerUser\n    countResponsesByCurrentUser\n    activeFrom\n    activeUntil\n    canRemove\n\n    languages {\n      title\n      language\n      canRemove\n    }\n  }\n"): (typeof documents)["\n  fragment EditSurveyPage on SurveyType {\n    slug\n    title(lang: $locale)\n    loginRequired\n    anonymity\n    maxResponsesPerUser\n    countResponsesByCurrentUser\n    activeFrom\n    activeUntil\n    canRemove\n\n    languages {\n      title\n      language\n      canRemove\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query EditSurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyPage\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query EditSurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          ...EditSurveyPage\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query SurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          loginRequired\n          anonymity\n          maxResponsesPerUser\n          countResponsesByCurrentUser\n\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query SurveyPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          loginRequired\n          anonymity\n          maxResponsesPerUser\n          countResponsesByCurrentUser\n\n          form(lang: $locale) {\n            title\n            description\n            fields\n            layout\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UpdateResponseDimensions($input: UpdateResponseDimensionsInput!) {\n    updateResponseDimensions(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation UpdateResponseDimensions($input: UpdateResponseDimensionsInput!) {\n    updateResponseDimensions(input: $input) {\n      response {\n        id\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query SurveyResponseDetail(\n    $eventSlug: String!\n    $surveySlug: String!\n    $responseId: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          slug\n          anonymity\n          dimensions {\n            title(lang: $locale)\n            slug\n            isMultiValue\n            values {\n              title(lang: $locale)\n              slug\n              color\n            }\n          }\n          response(id: $responseId) {\n            id\n            sequenceNumber\n            createdAt\n            createdBy {\n              displayName\n              email\n            }\n            language\n            values\n            form {\n              fields\n              layout\n            }\n            cachedDimensions\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query SurveyResponseDetail(\n    $eventSlug: String!\n    $surveySlug: String!\n    $responseId: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          slug\n          anonymity\n          dimensions {\n            title(lang: $locale)\n            slug\n            isMultiValue\n            values {\n              title(lang: $locale)\n              slug\n              color\n            }\n          }\n          response(id: $responseId) {\n            id\n            sequenceNumber\n            createdAt\n            createdBy {\n              displayName\n              email\n            }\n            language\n            values\n            form {\n              fields\n              layout\n            }\n            cachedDimensions\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation SubscribeToSurveyResponses($input: SubscriptionInput!) {\n    subscribeToSurveyResponses(input: $input) {\n      success\n    }\n  }\n"): (typeof documents)["\n  mutation SubscribeToSurveyResponses($input: SubscriptionInput!) {\n    subscribeToSurveyResponses(input: $input) {\n      success\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation UnsubscribeFromSurveyResponses($input: SubscriptionInput!) {\n    unsubscribeFromSurveyResponses(input: $input) {\n      success\n    }\n  }\n"): (typeof documents)["\n  mutation UnsubscribeFromSurveyResponses($input: SubscriptionInput!) {\n    unsubscribeFromSurveyResponses(input: $input) {\n      success\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment SurveyResponse on LimitedResponseType {\n    id\n    sequenceNumber\n    createdAt\n    createdBy {\n      displayName\n    }\n    language\n    values(keyFieldsOnly: true)\n    cachedDimensions(keyDimensionsOnly: true)\n  }\n"): (typeof documents)["\n  fragment SurveyResponse on LimitedResponseType {\n    id\n    sequenceNumber\n    createdAt\n    createdBy {\n      displayName\n    }\n    language\n    values(keyFieldsOnly: true)\n    cachedDimensions(keyDimensionsOnly: true)\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query FormResponses(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    profile {\n      forms {\n        surveys(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          anonymity\n\n          fields(lang: $locale, keyFieldsOnly: true)\n          dimensions {\n            slug\n            title(lang: $locale)\n            isKeyDimension\n\n            values {\n              slug\n              title(lang: $locale)\n              color\n            }\n          }\n\n          countResponses\n\n          responses(filters: $filters) {\n            ...SurveyResponse\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query FormResponses(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    profile {\n      forms {\n        surveys(eventSlug: $eventSlug) {\n          slug\n        }\n      }\n    }\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          anonymity\n\n          fields(lang: $locale, keyFieldsOnly: true)\n          dimensions {\n            slug\n            title(lang: $locale)\n            isKeyDimension\n\n            values {\n              slug\n              title(lang: $locale)\n              color\n            }\n          }\n\n          countResponses\n\n          responses(filters: $filters) {\n            ...SurveyResponse\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query SurveySummary(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          fields(lang: $locale)\n          summary(filters: $filters)\n          countFilteredResponses: countResponses(filters: $filters)\n          countResponses\n          dimensions {\n            slug\n            title(lang: $locale)\n            values {\n              slug\n              title(lang: $locale)\n            }\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query SurveySummary(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n    $filters: [DimensionFilterInput!]\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          title(lang: $locale)\n          fields(lang: $locale)\n          summary(filters: $filters)\n          countFilteredResponses: countResponses(filters: $filters)\n          countResponses\n          dimensions {\n            slug\n            title(lang: $locale)\n            values {\n              slug\n              title(lang: $locale)\n            }\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query SurveyThankYouPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          form(lang: $locale) {\n            title\n            thankYouMessage\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query SurveyThankYouPageQuery(\n    $eventSlug: String!\n    $surveySlug: String!\n    $locale: String\n  ) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        survey(slug: $surveySlug) {\n          form(lang: $locale) {\n            title\n            thankYouMessage\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  mutation CreateSurvey($input: CreateSurveyInput!) {\n    createSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"): (typeof documents)["\n  mutation CreateSurvey($input: CreateSurveyInput!) {\n    createSurvey(input: $input) {\n      survey {\n        slug\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment Survey on SurveyType {\n    slug\n    title(lang: $locale)\n    isActive\n    activeFrom\n    activeUntil\n    countResponses\n\n    languages {\n      language\n    }\n  }\n"): (typeof documents)["\n  fragment Survey on SurveyType {\n    slug\n    title(lang: $locale)\n    isActive\n    activeFrom\n    activeUntil\n    countResponses\n\n    languages {\n      language\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query Surveys($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        surveys(includeInactive: true) {\n          ...Survey\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query Surveys($eventSlug: String!, $locale: String) {\n    event(slug: $eventSlug) {\n      name\n\n      forms {\n        surveys(includeInactive: true) {\n          ...Survey\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query ProfileSurveyResponsePage($locale: String!, $responseId: String!) {\n    profile {\n      forms {\n        response(id: $responseId) {\n          id\n          createdAt\n          values\n\n          dimensions {\n            ...DimensionBadge\n          }\n\n          form {\n            slug\n            title\n            language\n            fields\n            layout\n            event {\n              slug\n              name\n            }\n            survey {\n              anonymity\n            }\n          }\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query ProfileSurveyResponsePage($locale: String!, $responseId: String!) {\n    profile {\n      forms {\n        response(id: $responseId) {\n          id\n          createdAt\n          values\n\n          dimensions {\n            ...DimensionBadge\n          }\n\n          form {\n            slug\n            title\n            language\n            fields\n            layout\n            event {\n              slug\n              name\n            }\n            survey {\n              anonymity\n            }\n          }\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment ProfileResponsesTableRow on ProfileResponseType {\n    id\n    createdAt\n    dimensions(keyDimensionsOnly: true) {\n      dimension {\n        slug\n        title(lang: $locale)\n      }\n\n      value {\n        slug\n        title(lang: $locale)\n        color\n      }\n    }\n    form {\n      slug\n      title\n      event {\n        slug\n        name\n      }\n    }\n  }\n"): (typeof documents)["\n  fragment ProfileResponsesTableRow on ProfileResponseType {\n    id\n    createdAt\n    dimensions(keyDimensionsOnly: true) {\n      dimension {\n        slug\n        title(lang: $locale)\n      }\n\n      value {\n        slug\n        title(lang: $locale)\n        color\n      }\n    }\n    form {\n      slug\n      title\n      event {\n        slug\n        name\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  query OwnFormResponses($locale: String!) {\n    profile {\n      forms {\n        responses {\n          ...ProfileResponsesTableRow\n        }\n      }\n    }\n  }\n"): (typeof documents)["\n  query OwnFormResponses($locale: String!) {\n    profile {\n      forms {\n        responses {\n          ...ProfileResponsesTableRow\n        }\n      }\n    }\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment DimensionBadge on ResponseDimensionValueType {\n    dimension {\n      slug\n      title(lang: $locale)\n    }\n\n    value {\n      slug\n      title(lang: $locale)\n      color\n    }\n  }\n"): (typeof documents)["\n  fragment DimensionBadge on ResponseDimensionValueType {\n    dimension {\n      slug\n      title(lang: $locale)\n    }\n\n    value {\n      slug\n      title(lang: $locale)\n      color\n    }\n  }\n"];

export function graphql(source: string) {
  return (documents as any)[source] ?? {};
}

export type DocumentType<TDocumentNode extends DocumentNode<any, any>> = TDocumentNode extends DocumentNode<  infer TType,  any>  ? TType  : never;