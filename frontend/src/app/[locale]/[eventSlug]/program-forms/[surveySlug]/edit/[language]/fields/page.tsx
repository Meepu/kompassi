import { notFound } from "next/navigation";

import ProgramFormEditorView from "../../ProgramFormEditorView";
import { updateSurveyFields } from "./actions";
import { graphql } from "@/__generated__";
import { getClient } from "@/apolloClient";
import { auth } from "@/auth";
import FormEditorWrapper from "@/components/forms/FormEditorWrapper";
import { validateFields } from "@/components/forms/models";
import SignInRequired from "@/components/SignInRequired";
import getPageTitle from "@/helpers/getPageTitle";
import { getTranslations } from "@/translations";

graphql(`
  fragment EditProgramFormFields on SurveyType {
    slug
    title(lang: $locale)
    canRemove

    form(lang: $language) {
      title
      language
      fields(enrich: false)
      canRemove
    }

    languages {
      language
    }
  }
`);

const query = graphql(`
  query EditProgramFormFieldsPage(
    $eventSlug: String!
    $surveySlug: String!
    $language: String!
    $locale: String
  ) {
    event(slug: $eventSlug) {
      name
      slug

      forms {
        survey(slug: $surveySlug, app: PROGRAM_V2) {
          ...EditProgramFormFields
        }
      }
    }
  }
`);

interface Props {
  params: {
    locale: string; // UI language
    eventSlug: string;
    surveySlug: string;
    language: string; // language code of form being edited
  };
}

export const revalidate = 0;

export async function generateMetadata({ params }: Props) {
  const { locale, eventSlug, surveySlug, language } = params;
  const translations = getTranslations(locale);

  // TODO encap
  const session = await auth();
  if (!session) {
    return translations.SignInRequired.metadata;
  }

  const t = translations.Survey;

  const { data } = await getClient().query({
    query,
    variables: { locale, eventSlug, surveySlug, language },
  });

  if (!data.event?.forms?.survey?.form) {
    notFound();
  }

  const title = getPageTitle({
    translations,
    event: data.event,
    subject: data.event.forms.survey.form.title,
    viewTitle: t.editSurveyPage.title,
  });

  return { title };
}

export default async function EditProgramFormFieldsPage({ params }: Props) {
  const { locale, eventSlug, surveySlug, language } = params;
  const translations = getTranslations(locale);
  const t = translations.Survey;
  const session = await auth();

  // TODO encap
  if (!session) {
    return <SignInRequired messages={translations.SignInRequired} />;
  }

  const { data } = await getClient().query({
    query,
    variables: { locale, eventSlug, surveySlug, language },
  });

  if (!data?.event?.forms?.survey?.form) {
    notFound();
  }

  const survey = data.event.forms.survey;
  const form = data.event.forms.survey.form;
  const activeTab = `fields-${language}`;

  validateFields(form.fields);

  return (
    <ProgramFormEditorView
      translations={translations}
      event={data.event}
      survey={survey}
      activeTab="properties"
    >
      <FormEditorWrapper
        initialFields={form.fields}
        messages={{
          FormEditor: translations.FormEditor,
          SchemaForm: translations.SchemaForm,
        }}
        onChange={updateSurveyFields.bind(
          null,
          eventSlug,
          surveySlug,
          language,
        )}
      />
    </ProgramFormEditorView>
  );
}
