// TODO: remove usePathname, make server component
"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { Translations } from "@/translations/en";
import { supportedLanguages } from "@/translations";

interface NavigationProps {
  translations: Translations;
}

export default function Navigation({ translations }: NavigationProps) {
  const { otherLanguage } = translations.LanguageSelection;
  let pathname = usePathname();

  // Remove the language prefix from the pathname
  // If we were using <Link>, Next.js would handle this for us
  // But that also sometimes preloads the link, causing a language change
  for (const supportedLanguage of supportedLanguages) {
    if (pathname.startsWith(`/${supportedLanguage}/`)) {
      pathname = pathname.slice(supportedLanguage.length + 1);
      break;
    }
  }

  // implemented in ../middleware.ts
  const languageToggleUri = `/${otherLanguage.code}${pathname}`;

  return (
    <div className="navbar navbar-dark bg-primary navbar-expand-lg">
      <div className="container-fluid">
        <Link href="/" className="navbar-brand">
          {translations.Brand.appName}
        </Link>
        <div className="navbar-nav ms-auto">
          <a
            href={languageToggleUri}
            className="nav-link"
            lang={otherLanguage.code}
          >
            {otherLanguage.nameInOtherLanguage}
          </a>
        </div>
      </div>
    </div>
  );
}
