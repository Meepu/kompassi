import Link from "next/link";
import { ReactNode } from "react";

import { payOrder } from "./actions";
import Section from "@/components/Section";
import OrderHeader from "@/components/tickets/OrderHeader";
import ProductsTable from "@/components/tickets/ProductsTable";
import ViewContainer from "@/components/ViewContainer";
import { getOrder } from "@/services/orders";
import { getTranslations } from "@/translations";

interface Props {
  params: {
    locale: string;
    eventSlug: string;
    orderId: string;
  };
}

export const revalidate = 0;

function formatOrderNumber(orderNumber: number) {
  return `#${orderNumber.toString().padStart(6, "0")}`;
}

/// NOTE: This page is on the Critical Path of the Hunger Games, so be extra mindful of performance.
/// Also this page can be accessed without authentication (ie. we don't know the accessor is the person who ordered)
/// so absolutely no PII.
export default async function OrderPage({ params }: Props) {
  const { locale, eventSlug, orderId } = params;
  const { order, event } = await getOrder(eventSlug, orderId);
  const translations = getTranslations(locale);
  const t = translations.Tickets;

  function ProfileLink({ children }: { children: ReactNode }) {
    return <Link href={`/${locale}/profile/orders`}>{children}</Link>;
  }

  return (
    <ViewContainer>
      <OrderHeader order={order} messages={t} locale={locale} event={event} />

      <ProductsTable order={order} messages={t} />

      {order.status == "PENDING" && (
        <Section>
          <form action={payOrder.bind(null, locale, eventSlug, orderId)}>
            <div className="d-grid gap-2">
              <button className="btn btn-primary btn-lg" type="submit">
                {t.Order.actions.pay}
              </button>
            </div>
          </form>
        </Section>
      )}

      <p>{t.Order.profileMessage(ProfileLink)}</p>
    </ViewContainer>
  );
}
