import Tabs, { Tab } from "@/components/ServerTabs";
import { Translations } from "@/translations/en";

export interface ProgramAdminTabsProps {
  eventSlug: string;
  active:
    | "programForms"
    | "offers"
    | "programItems"
    | "programHosts"
    | "dimensions"
    | "preferences";
  translations: Translations;
  queryString?: string;
}

export default function ProgramAdminTabs({
  eventSlug,
  translations,
  active,
  queryString,
}: ProgramAdminTabsProps) {
  const t = translations.Program;
  queryString = queryString ? "?" + queryString : "";

  const tabs: Tab[] = [
    {
      slug: "programForms",
      title: t.ProgramForm.listTitle,
      href: `/${eventSlug}/program-forms`,
    },
    {
      slug: "offers",
      title: t.Offer.listTitle,
      href: `/${eventSlug}/program-offers${queryString}`,
    },
    {
      slug: "programItems",
      title: t.adminListTitle,
      href: `/${eventSlug}/program-admin${queryString}`,
      disabled: true,
    },
    {
      slug: "programHosts",
      title: t.ProgramHost.listTitle,
      href: `/${eventSlug}/program-hosts${queryString}`,
      disabled: true,
    },
    {
      slug: "dimensions",
      title: translations.Dimension.listTitle,
      href: `/${eventSlug}/program-dimensions`,
      disabled: true,
    },
    {
      slug: "preview",
      title: t.actions.preview,
      href: `/${eventSlug}/program${queryString}`,
      disabled: true,
      // getTabHeader() {
      //   // Program view has no admin controls, so treat it as external for now
      //   return (
      //     <a
      //       className="nav-link"
      //       href={this.href}
      //       target="_blank"
      //       rel="noopener noreferrer"
      //     >
      //       {this.title}…
      //     </a>
      //   );
      // },
    },
    {
      slug: "preferences",
      title: t.actions.preferences,
      href: `/${eventSlug}/program-preferences`,
      disabled: true,
    },
  ];

  return <Tabs tabs={tabs} active={active} />;
}
