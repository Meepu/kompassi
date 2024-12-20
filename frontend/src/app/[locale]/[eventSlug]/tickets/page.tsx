import { createOrder } from "./actions";
import { getProducts } from "./service";
import ContactForm from "@/components/tickets/ContactForm";
import ViewContainer from "@/components/ViewContainer";
import ViewHeading from "@/components/ViewHeading";
import formatMoney from "@/helpers/formatMoney";
import getPageTitle from "@/helpers/getPageTitle";
import { getTranslations } from "@/translations";

interface Props {
  params: {
    locale: string;
    eventSlug: string;
  };
}

export async function generateMetadata({ params }: Props) {
  const { locale, eventSlug } = params;
  const translations = getTranslations(locale);
  const t = translations.Tickets;
  const { event } = await getProducts(eventSlug);

  const title = getPageTitle({ translations, event, viewTitle: t.title });

  return {
    title,
  };
}

export const revalidate = 1;

export default async function TicketsPage({ params }: Props) {
  const { locale, eventSlug } = params;
  const translations = getTranslations(locale);
  const t = translations.Tickets.Order;
  const producT = translations.Tickets.Product;
  const tickeT = translations.Tickets;
  const { event, products } = await getProducts(eventSlug);

  if (products.length === 0) {
    return (
      <ViewContainer>
        <ViewHeading>
          {producT.noProducts.title}
          <ViewHeading.Sub>{producT.forEvent(event.name)}</ViewHeading.Sub>
        </ViewHeading>
        <p>{producT.noProducts.message}</p>
      </ViewContainer>
    );
  }

  return (
    <ViewContainer>
      <ViewHeading>
        {tickeT.title}
        <ViewHeading.Sub>{tickeT.forEvent(event.name)}</ViewHeading.Sub>
      </ViewHeading>

      <form action={createOrder.bind(null, locale, eventSlug)}>
        <table className="table table-striped mt-4 mb-4">
          <thead>
            <tr className="row">
              <th className="col-8">{producT.attributes.product}</th>
              <th className="col">{producT.attributes.unitPrice}</th>
              <th className="col">{producT.attributes.quantity.title}</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => (
              <tr key={product.id} className="row">
                <td className="col-8">
                  <p>
                    <strong>{product.title}</strong>
                  </p>
                  {product.description}
                </td>
                <td className="col fs-4">{formatMoney(product.price)}</td>
                <td className="col">
                  <label
                    htmlFor={`quantity-${product.id}`}
                    className="visually-hidden"
                  >
                    {producT.attributes.quantity.title}
                  </label>
                  <input
                    type="number"
                    className="form-control"
                    id={`quantity-${product.id}`}
                    name={`quantity-${product.id}`}
                    defaultValue={0}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        <h2 className="mb-4">{t.contactForm.title}</h2>
        <ContactForm messages={translations} />

        <div className="d-grid gap-2 mb-4">
          <button className="btn btn-primary btn-lg" type="submit">
            {t.actions.purchase.title}
          </button>
        </div>
      </form>
    </ViewContainer>
  );
}
