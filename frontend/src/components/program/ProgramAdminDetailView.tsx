import Link from "next/link";
import { ReactNode } from "react";
import ProgramAdminDetailTabs, {
  ProgramAdminTab,
} from "./ProgramAdminDetailTabs";
import ViewContainer from "@/components/ViewContainer";
import ViewHeading, {
  ViewHeadingActions,
  ViewHeadingActionsWrapper,
} from "@/components/ViewHeading";
import type { Translations } from "@/translations/en";

interface Event {
  slug: string;
  name: string;
}

interface Program {
  slug: string;
  title: string;
}

interface Props {
  event: Event;
  program: Program;
  translations: Translations;
  active: ProgramAdminTab;
  children?: ReactNode;
  actions?: ReactNode;
}

export default function ProgramAdminDetailView({
  event,
  program,
  translations,
  active,
  children,
  actions,
}: Props) {
  const t = translations.Program;

  return (
    <ViewContainer>
      <Link className="link-subtle" href={`/${event.slug}/program-admin`}>
        &lt; {t.actions.returnToProgramAdminList(event.name)}
      </Link>

      <ViewHeadingActionsWrapper>
        <ViewHeading>
          {program.title}
          <ViewHeading.Sub>{t.inEvent(event.name)}</ViewHeading.Sub>
        </ViewHeading>
        <ViewHeadingActions>{actions}</ViewHeadingActions>
      </ViewHeadingActionsWrapper>

      <ProgramAdminDetailTabs
        eventSlug={event.slug}
        programSlug={program.slug}
        translations={translations}
        active={active}
      />

      {children}
    </ViewContainer>
  );
}
