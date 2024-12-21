// Translators: Kirsi Västi, Calle Tengman, Santtu Pajukanta

import { ReactNode, JSX } from "react";
import type { Translations } from "./en";

/// Mark untranslated English strings with this
/// Eg.
/// { foo: UNTRANSLATED("bar") }
function UNTRANSLATED<T>(wat: T): T {
  return wat;
}

/// Mark strings to be checked by a native speaker / more experienced translator with this
function UNSURE<T>(wat: T): T {
  return wat;
}

const translations: Translations = {
  Common: {
    ok: "OK",
    cancel: "Avbryt",
    submit: "Skicka",
    search: "Sök",
    somethingWentWrong:
      "Något gick fel. Det kan finnas ytterligare information i JavaScript-konsolen.",
    actions: "Funktioner",
    standardActions: {
      open: "Öppna",
      edit: "Ändra",
      delete: "Radera",
      create: "Skapa",
      close: "Stäng",
    },
    boolean: {
      true: "Ja",
      false: "Nej",
    },
  },
  Profile: {
    attributes: {
      displayName: {
        title: "Namn",
      },
      email: {
        title: "E-postadress",
      },
    },
    keysView: UNTRANSLATED({
      title: "Encryption keys",
      description:
        "In some cases, confidential data is encrypted in Kompassi using asymmetric encryption. " +
        "If you need to be the recipient of such confidential information, you need to have a key pair. " +
        "You can generate one below. " +
        "Generating a key pair requires your password as the private key will be encrypted with it. " +
        "In the future, we will allow advanced users to use keys stored on their own devices only, " +
        "so that the private key never leaves the device.",
      resetPasswordWarning: (
        <>
          <strong>Warning!</strong> If you forget your password and resert it,
          you will lose your encryption keys and will no longer be able to
          access data encrypted to them.
        </>
      ),
      attributes: {
        id: {
          title: "Key ID",
        },
        createdAt: {
          title: "Created at",
        },
        actions: {
          title: "Actions",
        },
        password: {
          title: "Password",
          helpText: "Enter your password to encrypt the private key.",
        },
      },
      actions: {
        generate: {
          title: "Generate key pair",
          enterPassword: "Enter your password to encrypt the private key.",
          modalActions: {
            submit: "Generate",
            cancel: "Cancel",
          },
        },
        revoke: {
          title: "Revoke key pair",
          confirmation: (formattedCreatedAt: string) => (
            <>
              Are you sure you want to revoke the key pair that was created on{" "}
              <strong>{formattedCreatedAt}</strong>? Once revoked, information
              that was encrypted with the private key will no longer be
              accessible. This action cannot be undone.
            </>
          ),
          modalActions: {
            submit: "Revoke",
            cancel: "Cancel",
          },
        },
      },
    }),
  },
  // Note that this also defines the type for the messages object that can be passed to the InterceptingRouteModal component
  Modal: {
    submit: "Skicka",
    cancel: "Avbryt",
  },
  DataTable: {
    create: "Skapa",
  },
  Event: {
    title: "Evenemang",
    headline: "Datum och plats",
    name: "Namn",
    workInProgress:
      "Kompassi v2 är ett pågående arbete. Detta är inte den färdiga förstasidan, utan snarare en demo av tabellkomponenten.",
  },
  UserMenu: {
    tickets: "Biljetter",
    responses: "Enkätsvar",
    keys: UNSURE("Krypteringsnycklar"),
    signIn: "Logga in",
    signOut: "Logga ut",
  },
  NotFound: {
    notFoundHeader: "Sidan hittades inte",
    notFoundMessage:
      "Adressen överensstämmer inte med något av de kända adressmönstren. Vänligen dubbelkolla adressen.",
  },
  SchemaForm: {
    submit: "Skicka",
    warnings: {
      noFileUploaded: "Inga filer.",
    },
  },
  MainView: {
    defaultErrorMessage:
      "Något gick fel. Det kan finnas ytterligare information i JavaScript-konsolen.",
  },
  FormEditor: {
    editField: "Ändra fält",
    moveUp: "Flytta upp",
    moveDown: "Flytta ner",
    removeField: "Ta bort fält",
    addFieldAbove: "Lägg till fält ovan",
    addField: "Lägg till fält",
    save: "Spara formulär",
    cancel: "Gå tillbaka utan att spara",
    open: "Öppna formulär",
    saveFailedErrorMessage:
      "Något gick fel när formuläret sparades. Det kan finnas ytterligare information i JavaScript-konsolen.",

    tabs: {
      design: "Ändra",
      preview: "Förhandsvisning",
      properties: "Inställningar",
    },

    attributes: {
      title: {
        title: "Titel",
        helpText: "Människoläsbar titel. Visas för slutanvändaren.",
      },
      description: {
        title: "Beskrivning",
        helpText: "Visas ovanför formuläret.",
      },
      thankYouMessage: {
        title: "Tack meddelande",
        helpText:
          "Visas efter att formuläret har skickats. Om ett tackmeddelande inte är inställt visas standardmeddelandet.",
      },
    },

    editFieldForm: {
      slug: {
        title: "Tekniskt namn",
        helpText: UNSURE(
          "Maskinläsbart fältnamn. Giltiga tecken: bokstäverna A-Za-z, siffrorna 0-9, understreck _. Får inte börja med en siffra. Måste vara densamma i alla språkversioner.",
        ),
      },
      title: {
        title: "Titel",
        helpText:
          "Människligt läsbar fältetikett. Om den inte är inställd, används fältnamn som standard.",
      },
      helpText: {
        title: "Hjälptext",
        helpText: "Visas under fältet.",
      },
      required: {
        title: "Obligatoriskt",
      },
      choices: UNTRANSLATED({
        title: "Choices",
        helpText:
          'Each line should contain one choice in the form of "slug: Choice shown to the user".',
      }),
      questions: UNTRANSLATED({
        title: "Questions",
        helpText:
          'Each line should contain one question in the form of "slug: Question shown to the user".',
      }),
      encryptTo: UNTRANSLATED({
        title: "Encrypt to",
        helpText:
          "If you want to encrypt the responses to this field, enter the user names of users who should be able to decrypt the responses (one per line). These users must have a key pair generated in their profile.",
      }),
    },

    fieldTypes: {
      SingleLineText: "Textfält med en rad",
      MultiLineText: " Textfält med flera rader",
      Divider: "Separatorlinje",
      StaticText: "Statisk text",
      Spacer: "Tomt utrymme",
      SingleCheckbox: "Enkel kryssruta",
      SingleSelect: "Listrutan (ett val)",
      MultiSelect: "Listrutan (flera val)",
      RadioMatrix: "Urvalsmatris",
      FileUpload: "Skicka fil",
      NumberField: "Nummer",
      DecimalField: "Decimal",
      DateField: "Datum",
      DateTimeField: "Datum och tid",
      TimeField: "Tid",
    },

    removeFieldModal: {
      title: "Bekräfta borttagning av fält",
      message: "Ta bort det valda fältet?",
      actions: {
        submit: "Ta bort",
        cancel: "Avbryt",
      },
    },

    editFieldModal: {
      title: "Redigera fält",
      actions: {
        submit: "Spara fältet",
        cancel: "Avbryt",
      },
    },
  },

  SplashView: {
    engagement: (
      <>
        Stanna kvar medan vi återimplementerar nyckelfunktionerna i{" "}
        <strong style={{ whiteSpace: "nowrap" }}>
          Kompassi Event Management System
        </strong>{" "}
        använder modern webbteknik för bättre användarupplevelse och bättre
        anpassning för självbetjäning!
      </>
    ),
    backToKompassi: "Tillbaka till Kompassi",
  },

  EventsView: {
    title: "Evenemang",
  },

  Tickets: UNTRANSLATED({
    title: "Purchase tickets",
    forEvent: (eventName: string) => <>for {eventName}</>,
    returnToTicketsPage: "Return to the tickets page",
    Product: {
      listTitle: "Products",
      forEvent: (eventName: string) => <>for {eventName}</>,
      noProducts: {
        title: "No products available",
        message: "There are no products available for purchase at the moment.",
      },
      actions: {
        editProduct: "Edit product",
        newProduct: "New product",
        saveProduct: "Save product",
        unpublishAllProducts: "Unpublish all products",
        viewOldVersion: "View",
      },
      attributes: {
        product: "Product",
        title: "Title",
        createdAt: "Created at",
        unitPrice: "Unit price",
        quantity: {
          title: "Quantity",
          unit: "pcs",
        },
        total: "Total",
        description: "Description",
        isAvailable: {
          title: "Availability schedule",
          untilFurtherNotice: "Available until further notice",
          untilTime: (formattedTime: String) =>
            `Available until ${formattedTime}`,
          openingAt: (formattedTime: String) =>
            `Will become available at ${formattedTime}`,
          notAvailable: "Not available",
        },
        maxPerOrder: {
          title: "Maximum amount per order",
          helpText: "No more than this amount will be sold in one order.",
        },
        eticketsPerProduct: {
          title: "Number of electronic tickets per product",
          helpText:
            "The number of electronic ticket codes that will be generated for each instance of the product sold. If set to 0, no electronic tickets will be generated.",
        },
        availableFrom: {
          title: "Available from",
          helpText:
            "In order for the product to become available, this field must be set and the time set herein must have passed.",
        },
        availableUntil: {
          title: "Available until",
          helpText:
            "If set, the product will no longer be available after this time.",
        },
        countPaid: "Paid",
        countReserved: {
          title: "Sold",
          description:
            "In addition to paid orders, includes those orders that have been confirmed but not yet paid.",
        },
        countAvailable: "Remaining",
        countTotal: "Total",
        actions: "Actions",
        totalReserved: "Total sold",
        totalPaid: "Total paid",
        revisions: {
          title: "Revisions of this product",
          description:
            "If a product is edited after being sold, a new revision will be created that will replace the product in the shop. Setting the availability schedule or quotas will not create a new revision.",
          current: "Current",
        },
        quotas: {
          title: "Quotas",
          helpText:
            "Quotas determine how many pieces of a product may be sold. A product may use multiple quotas; the quota that has the least stock determines the availability of the product. You can edit and create new quotas on the Quotas tab.",
        },
        selectedQuotas: "Selected quotas",
        soldOut: "Utsålt",
      },
    },
    Quota: {
      listTitle: "Quotas",
      singleTitle: "Quota",
      forEvent: (eventName: string) => <>for {eventName}</>,
      actions: {
        newQuota: "New quota",
        editQuota: "Edit quota",
        saveQuota: "Save quota",
      },
      attributes: {
        name: "Name",
        countTotal: {
          title: "Quota",
          helpText: (countReserved: number) =>
            `How many units of products using this quota may at most be sold. There are currently ${countReserved} units sold; the quota cannot be adjusted lower than that.`,
        },
        totalReserved: "Total sold",
        products: {
          title: "Products using this quota",
          helpText:
            "A product may use multiple quotas; the quota that has the least stock determines the availability of the product.",
        },
      },
    },
    Order: {
      listTitle: "Beställningar",
      singleTitle: (orderNumber: string, paymentStatus: string) =>
        `Beställning ${orderNumber} (${paymentStatus})`,
      forEvent: (eventName: string) => <>for {eventName}</>,
      contactForm: {
        title: "Contact information",
      },
      profileMessage: (
        ProfileLink: ({ children }: { children: ReactNode }) => JSX.Element,
      ) => (
        <>
          If you have a user account with the email address you used to place
          this order, you can also view your order and download electronic
          tickets from your <ProfileLink>profile</ProfileLink>.
        </>
      ),
      attributes: {
        orderNumberAbbr: "Best.nr.",
        orderNumberFull: "Beställningsnummer",
        createdAt: "Order date",
        eventName: "Event",
        totalPrice: "Total price",
        actions: "Actions",
        totalOrders: (numOrders: number) => (
          <>
            Total {numOrders} order{numOrders === 1 ? "" : "s"}.
          </>
        ),
        firstName: {
          title: "First name",
        },
        lastName: {
          title: "Last name",
        },
        displayName: {
          title: "Customer name",
        },
        email: {
          title: "Email",
          helpText:
            "Check the email address carefully! Your tickets will be sent to this address.",
        },
        phone: {
          title: "Phone number",
        },
        acceptTermsAndConditions: {
          title: "Terms and conditions accepted",
          checkboxLabel(url: string) {
            return (
              <>
                I accept the{" "}
                <a href={url} target="_blank" rel="noopener noreferrer">
                  terms and conditions
                </a>{" "}
                (required).
              </>
            );
          },
        },
        provider: {
          title: "Betalningsmetod",
          choices: {
            NONE: "Ingen (gratis)",
            PAYTRAIL: "Paytrail",
            STRIPE: "Stripe",
          },
        },
        status: {
          title: "Status",
          choices: {
            NOT_STARTED: {
              title: "Your order is awaiting payment",
              shortTitle: "Not started",
              message:
                "Your order has been confirmed and the products have been reserved to you, but we have not yet received your payment. Please use the button below to pay for your order as soon as possible. Unpaid orders will be eventually cancelled.",
            },
            PENDING: {
              title: "Your order is awaiting payment",
              shortTitle: "Awaiting payment",
              message:
                "Your order has been confirmed and the products have been reserved to you, but we have not yet received your payment. Please use the button below to pay for your order as soon as possible. Unpaid orders will be eventually cancelled.",
            },
            FAILED: {
              title: "Payment failed",
              shortTitle: "Payment failed",
              message:
                "The payment for your order failed or was cancelled. Please try again. Unpaid orders will be eventually cancelled.",
            },
            PAID: {
              title: "Your order is complete!",
              shortTitle: "Paid",
              message:
                "Your order has been paid. You will receive a confirmation email shortly. If there are electronic tickets, they will be attached to the email.",
            },
            CANCELLED: {
              title: "Your order has been cancelled",
              shortTitle: "Cancelled",
              message:
                "Your order has been cancelled. If there were electronic tickets in the order, they have been invalidated. If you believe this is an error, please contact the event organizer.",
            },
            REFUND_REQUESTED: {
              title: "Your order has been refunded",
              shortTitle: "Refund requested",
              message:
                "Your order has been refunded. If there were electronic tickets in the order, they have been invalidated. If you believe this is an error, please contact the event organizer.",
            },
            REFUND_FAILED: {
              title: "Your order has been refunded",
              shortTitle: "Refund failed",
              message:
                "Your order has been refunded. If there were electronic tickets in the order, they have been invalidated. If you believe this is an error, please contact the event organizer.",
            },
            REFUNDED: {
              title: "Your order has been refunded",
              shortTitle: "Refunded",
              message:
                "Your order has been refunded. If there were electronic tickets in the order, they have been invalidated. If you believe this is an error, please contact the event organizer.",
            },
          },
        },
      },
      errors: {
        NOT_ENOUGH_TICKETS: {
          title: "Not enough tickets",
          message:
            "One or more of the products you tried to purchase are no longer available in the quantity you requested.",
        },
        INVALID_ORDER: {
          title: "Invalid order",
          message:
            "The details you entered on the order page were not accepted. Please check your order and try again.",
        },
        NO_PRODUCTS_SELECTED: {
          title: "No products selected",
          message: "Please select at least one product to purchase.",
        },
        UNKNOWN_ERROR: {
          title: "Error processing order",
          message:
            "An error occurred while processing your order. Please try again later.",
        },
        ORDER_NOT_FOUND: {
          title: "Order not found",
          message:
            "The order you are trying to view does not exist or is not associated with your user account.",
          actions: {
            returnToOrderList: "Return to list of orders",
            returnToTicketsPage: "Return to the tickets page",
          },
        },
      },
      actions: {
        purchase: "Bekräfta beställning och fortsätt till betalning",
        pay: "Fortsätt till betalning",
        viewTickets: "Se biljetter",
        newOrder: "Ny beställning",
        search: "Sök beställningar",
        saveContactInformation: "Spara kontaktuppgifter",
        resendOrderConfirmation: {
          title: "Resend order confirmation",
          message: (emailAddress: string) => (
            <>
              <p>
                Are you sure you want to resend the order confirmation email
                (incl. electronic tickets, if any) to the customer?
              </p>
              <p>
                The confirmation email will be sent to the following address:{" "}
                <strong>{emailAddress}</strong>
              </p>
              <p>
                <strong>NOTE:</strong> If you are changing the email address,
                please make sure to remember to save contact information before
                resending the confirmation.
              </p>
            </>
          ),
          modalActions: {
            submit: "Resend",
            cancel: "Close without resending",
          },
        },
        cancelAndRefund: {
          title: "Cancel and refund",
          message: (
            <>
              <p>This will</p>
              <ol>
                <li>mark the order as cancelled,</li>
                <li>invalidate any electronic tickets,</li>
                <li>send a cancellation notice to the customer, and</li>
                <li>request the payment processor to refund the payment.</li>
              </ol>
              <p>
                <strong>NOTE:</strong> The refund may fail if there are not
                sufficient funds deposited with the payment processor. In this
                case, you need to transfer funds and complete the refund via the
                merchant panel of the payment processor.
              </p>
            </>
          ),
          modalActions: {
            submit: "Cancel order and attempt refund",
            cancel: "Close without cancelling",
          },
        },
        cancelWithoutRefunding: {
          title: "Cancel without refunding",
          message: (
            <>
              <p>This will</p>
              <ol>
                <li>mark the order as cancelled,</li>
                <li>invalidate any electronic tickets, and</li>
                <li>send a cancellation notice to the customer.</li>
              </ol>
              <p>
                <strong>NOTE:</strong> No automatic refund will be made. If the
                payment needs to be refunded in part or in full, you will need
                to do this via the merchant panel of the payment processor, or
                use the &quot;Cancel and refund&quot; function.
              </p>
            </>
          ),
          modalActions: {
            submit: "Cancel order without refunding",
            cancel: "Close without cancelling",
          },
        },
      },
    },
    PaymentStamp: UNTRANSLATED({
      listTitle: "Payment stamps",
      attributes: {
        createdAt: "Timestamp",
        correlationId: "Correlation ID",
        type: {
          title: "Type",
          choices: {
            ZERO_PRICE: "Zero price",
            CREATE_PAYMENT_REQUEST: "Create payment – Request",
            CREATE_PAYMENT_SUCCESS: "Create payment – OK",
            CREATE_PAYMENT_FAILURE: "Create payment – Failed",
            PAYMENT_REDIRECT: "Payment redirect",
            PAYMENT_CALLBACK: "Payment callback",
            CANCEL_WITHOUT_REFUND: "Cancel without refund",
            CREATE_REFUND_REQUEST: "Create refund – Request",
            CREATE_REFUND_SUCCESS: "Create refund – OK",
            CREATE_REFUND_FAILURE: "Create refund – Failed",
          },
        },
      },
    }),
    Receipt: UNTRANSLATED({
      listTitle: "Receipts",
      attributes: {
        id: "Correlation ID",
        createdAt: "Sent at",
        type: {
          title: "Type",
          choices: {
            PAID: "Order confirmation",
            CANCELLED: "Order cancellation",
            REFUNDED: "Order refund",
          },
        },
        status: {
          title: "Status",
          choices: {
            REQUESTED: "Requested",
            PROCESSING: "Processing",
            FAILURE: "Failed",
            SUCCESS: "Sent",
          },
        },
      },
    }),
    profile: {
      title: "Ticket orders",
      message:
        "Here you can see your ticket orders made in 2025 and later. You can pay for unpaid orders and download your electronic tickets here.",
      haveUnlinkedOrders: {
        title: "Confirm your email address to see more orders",
        message:
          "There are ticket orders associated with your email address that are not linked to your user account. Confirm your email address to see these orders.",
      },
      actions: {
        confirmEmail: {
          title: "Confirm email address",
          description:
            "An email will be sent to the email address of your user account. Follow the instructions in the email to confirm your email address and see the rest of your orders.",
          modalActions: {
            submit: "Send confirmation message",
            cancel: "Cancel",
          },
        },
      },
      noOrders:
        "There are no orders associated with your user account to show.",
    },
    admin: {
      title: "Biljettbutikens admin",
      tabs: {
        orders: "Beställningar",
        products: "Produkter",
        quotas: "Kvoter",
        reports: "Rapporter",
        ticketControl: "Biljettkontroll",
      },
    },
  }),

  Program: UNSURE({
    listTitle: "Program",
    singleTitle: "Program",
    inEvent: (eventName: string) => <>i {eventName}</>,
    attributes: {
      title: "Rubrik",
      placeAndTime: "Plats och tid",
      actions: "Funktioner",
    },
    actions: {
      returnToProgramList: (eventName: string) =>
        `Tillbaka till programmet för ${eventName}`,
      addTheseToCalendar: "Lägg till dessa program i kalendern",
      addThisToCalendar: "Lägg till detta program i kalendern",
      signUpForThisProgram: "Anmäl dig till detta program",
    },
    favorites: {
      markAsFavorite: "Markera som favorit",
      unmarkAsFavorite: "Avmarkera som favorit",
      signInToAddFavorites:
        "Genom att logga in kan du markera program som favoriter, filtrera program efter favoriter och lägga till dina favoritprogram i kalendern.",
    },
    filters: {
      showOnlyFavorites: "Visa endast favoriter",
      hidePastPrograms: "Dölj förflutna program",
    },
    tabs: {
      cards: "Kort",
      table: "Tabell",
    },
    feedback: UNSURE({
      viewTitle: "Ge feedback",
      notAcceptingFeedback: "Det här programmet tar inte emot feedback.",
      fields: {
        feedback: {
          title: "Feedback",
          helpText:
            "Hur gillade du programmet? Var snäll och konstruktiv och empatisk mot programvärdarna :) Din feedback kommer att delas med programvärdarna.",
        },
        kissa: {
          title: "Vilket djur säger mjau?",
          helpText:
            "Vänligen svara för att bevisa att du inte är en robot. Tips: Katt.",
        },
      },
      actions: {
        returnToProgram: "Tillbaka till programmet",
        submit: "Skicka feedback",
      },
      anonymity: {
        title: "Koppla ditt svar till dig",
        description:
          "Om du ger feedback på programmet medan du är inloggad kommer ditt användarkonto att kopplas till din feedback. Ditt användarkonto kommer dock inte att delas med programvärdarna.",
      },
      thankYou: {
        title: "Tack för din feedback!",
        description: "Din feedback har registrerats.",
      },
    }),
  }),

  NewProgramView: {
    title: "Erbjud ett program",
    engagement: (eventName: string) => (
      <>
        Tack för ditt intresse för att erbjuda program till {eventName}! Snälla
        börja med att välja vilken typ av program du vill erbjuda nedan.
      </>
    ),
    selectThisProgramType: "Välj denna programtyp",
    backToProgramFormSelection: "Tillbaka till val av programtyp",
    forEvent: (eventName: string) => <>för {eventName}</>,
    submit: "Skicka",
  },

  Survey: {
    listTitle: "Enkäter",
    singleTitle: "Enkät",
    forEvent: (eventName: string) => <>för {eventName}</>,
    surveyTableFooter: (count: number) => (
      <>
        {count} enkät{count === 1 ? "" : "er"}.
      </>
    ),
    responseListTitle: "Svar",
    responseDetailTitle: "Svar",
    ownResponsesTitle: "Mina svar",
    showingResponses: (filteredCount: number, totalCount: number) => (
      <>
        Visar {filteredCount} svar (totalt {totalCount}).
      </>
    ),
    dimensionTableFooter: (countDimensions: number, countValues: number) => (
      <>
        Total {countDimensions} dimension{countDimensions === 1 ? "" : "er"},{" "}
        {countValues} värde{countValues === 1 ? "" : "er"}.
      </>
    ),
    summaryOf: (filteredCount: number, totalCount: number) => (
      <>
        Sammanfattning av {filteredCount} svar (totalt {totalCount}).
      </>
    ),
    theseProfileFieldsWillBeShared: UNSURE(
      "Då du skickar in denna enkät, kommer följande information att delas med enkätägaren:",
    ),
    correctInYourProfile: UNSURE((profileLink: string) => (
      <>
        Om dessa uppgifter inte är korrekta, vänligen korrigera dem i din{" "}
        <a href={profileLink} target="_blank" rel="noopener noreferrer">
          profil
        </a>{" "}
        (öppnas i ny flik).
      </>
    )),

    attributes: {
      slug: {
        title: "Tekniskt namn",
        helpText:
          "Ett maskinläsbart namn för frågan. Det tekniska namnet måste vara unikt för evenemanget. Det tekniska namnet kan inte ändras efter skapande.",
      },
      title: "Titel",
      isActive: {
        title: "Tar emot svar",
        untilFurtherNotice: "Öppet tills vidare",
        untilTime: (formattedTime) => `Öppet till ${formattedTime}`,
        openingAt: (formattedTime) => `Öppnar vid ${formattedTime}`,
        closed: "Stängt",
      },
      activeFrom: {
        title: "Öppet från",
        helpText:
          "Om detta är inställt kommer enkäten att börja acceptera svar vid denna tidpunkt.",
      },
      activeUntil: {
        title: "Stänger",
        helpText:
          "Om detta är inställt kommer enkäten att sluta acceptera svar vid denna tidpunkt.",
      },
      countResponses: "Svaren",
      languages: "Språk",
      actions: "Actions",
      anonymity: {
        secondPerson: {
          title: "Koppla ditt svar till dig",
          choices: {
            HARD: "Svaren är anonyma. Du kan inte återvända för att se eller redigera dina svar.",
            SOFT: "Om du svarar på den här enkäten medan du är inloggad kommer den att kopplas till ditt användarkonto, så att du kan återvända för att se eller redigera dina svar, men din identitet kommer inte att delas med enkätägaren.",
            NAME_AND_EMAIL:
              "Om du svarar på den här enkäten medan du är inloggad kommer den att kopplas till ditt användarkonto. Ditt namn och e-postadress kommer att delas med enkätägaren. Du kan återvända för att se eller redigera dina svar.",
          },
        },
        thirdPerson: {
          title: "Koppla svar till användare",
          choices: {
            HARD: "Svaren är anonyma. Användare kan inte återvända för att se eller redigera sina svar.",
            SOFT: "Om användaren svarar på den här enkäten medan hen är inloggad kommer deras svar att kopplas till deras användarkonto, så att de kan återvända för att se eller redigera sina svar, men deras identiteter kommer inte att delas med dig.",
            NAME_AND_EMAIL:
              "Om användaren svarar på den här enkäten medan hen är inloggad kommer deras svar att kopplas till deras användarkonto. Deras namn och e-postadresser kommer att delas med dig. De kan återvända för att se eller redigera sina svar.",
          },
        },
      },
      dimensions: "Dimensionerna",
      dimension: "Dimension",
      values: "Värden",
      value: "Värde",
      sequenceNumber: "Sekvensnummer",
      createdAt: "Sändningstid",
      createdBy: "Avsändare",
      event: "Evenemang",
      formTitle: "Enkätens titel",
      language: "Språk",
      choice: "Val",
      question: "Fråga",
      countMissingResponses: "Inget svar",
      percentageOfResponses: "Andel av svar",
      technicalDetails: "Tekniska detaljer",
      loginRequired: {
        title: "Inloggning krävs",
        helpText:
          "Om detta väljs, kräver det att du loggar in för att svara på enkäten.",
      },
      maxResponsesPerUser: {
        title: "Maximalt antal svar per användaren",
        helpText:
          "Det maximala antalet svar från en enskild användare på denna enkät. Om värdet är satt till 0 är beloppet inte begränsat. Observera att detta endast påverkar inloggade användare. För att begränsningen ska fungera måste svaret på enkäten begränsas till inloggade användare.",
      },
    },
    actions: {
      createSurvey: "Skapa en enkät",
      fillIn: {
        title: "Fyll i",
        disabledTooltip: "Stängd enkät kan inte fyllas i",
      },
      share: {
        title: "Dela",
        tooltip: "Kopiera länk till urklipp",
        success: "En länk till enkäten har kopierats till urklipp.",
      },
      viewResponses: "Visa svar",
      toggleSubscription: "Meddela mig om nya svar",
      submit: "Skicka",
      downloadAsExcel: "Ladda ner som Excel",
      returnToResponseList: "Tillbaka till listan över svar",
      returnToSurveyList: "Tillbaka till listan över enkäter",
      returnToDimensionList: "Tillbaka till dimensionslistan",
      saveDimensions: "Spara dimensioner",
      saveProperties: "Spara inställningar",
      addDimension: "Lägg till dimension",
      addDimensionValue: "Lägg till värde",
      deleteDimension: {
        title: "Radera dimension",
        cannotRemove:
          "En dimension kan inte raderas om den redan är kopplad till en enkät.",
        confirmation: (dimensionTitle: string) => (
          <>
            Radera dimension <strong>{dimensionTitle}</strong> med alla val?
          </>
        ),
        modalActions: {
          submit: "Radera",
          cancel: "Avbryt",
        },
      },
      deleteDimensionValue: {
        title: "Radera val",
        cannotRemove:
          "Ett val kan inte raderas om det redan är kopplat till en enkät.",
        confirmation: (dimensionTitle: string, valueTitle: string) => (
          <>
            Radera val <strong>{dimensionTitle}</strong> från dimensionen{" "}
            <strong>{valueTitle}</strong>?
          </>
        ),
      },
      deleteSurvey: {
        title: "Radera enkät",
        cannotRemove: "En enkät som redan har fått svar kan inte raderas.",
        confirmation: (surveyTitle: string) => (
          <>
            Är du säker på att du vill ta bort enkäten{" "}
            <strong>{surveyTitle}</strong>?
          </>
        ),
        modalActions: {
          submit: "Radera",
          cancel: "Avbryt",
        },
      },
      editDimension: "Ändra dimensionen",
      editDimensionValue: "Ändra val",
      editSurvey: "Ändra",
    },
    tabs: {
      summary: "Sammanfattning",
      responses: "Svaren",
      properties: "Frågeinställningar",
      addLanguage: "Lägg till språkversion",
      texts: (languageName: string) => `Texter (${languageName})`,
      fields: (languageName: string) => `Fält (${languageName})`,
    },
    thankYou: {
      title: "Tack för dina svar!",
      defaultMessage:
        "Dina svar har registrerats. Du kan nu stänga den här fliken.",
    },
    maxResponsesPerUserReached: {
      title: "Maximalt antal svar nått",
      defaultMessage: (
        maxResponsesPerUser: number,
        countResponsesByCurrentUser: number,
      ) =>
        `Du har redan skickat ${countResponsesByCurrentUser} svar${
          countResponsesByCurrentUser === 1 ? "" : "en"
        } till denna undersökning. Det maximala antalet svar per användare är ${maxResponsesPerUser}.`,
    },
    warnings: {
      choiceNotFound:
        "Valet hittades inte. Det kan ha tagits bort efter att detta svar skickades.",
    },
    checkbox: {
      checked: "Valt",
      unchecked: "Icke valt",
    },
    addLanguageModal: {
      language: {
        title: "Språk",
        helpText: "Endast språk som stöds kan läggas till.",
      },
      copyFrom: {
        title: "Börja från språkversionen",
        helpText:
          "En ny språkversion skapas baserat på den valda språkversionen. Du kan också välja att börja med ett tomt formulär.",
      },
      actions: {
        submit: "Fortsätt",
        cancel: "Avbryt",
      },
    },
    deleteLanguageModal: {
      title: "Radera språkversionen",
      confirmation: (languageName: string) => (
        <>
          Är du säker på att du vill radera språkversionen{" "}
          <strong>{languageName}</strong>?
        </>
      ),
      modalActions: {
        submit: "Radera",
        cancel: "Avbryt",
      },
    },
    editDimensionModal: {
      editTitle: "Ändra dimensionen",
      addTitle: "Lägg till dimensionen",
      actions: {
        submit: "Spara dimensionen",
        cancel: "Avbryt",
      },
      attributes: {
        slug: {
          title: "Tekniskt namn",
          // TODO add pattern for slug and document it in helpText
          helpText:
            "Ett maskinläsbart, kort namn på en dimension. Det tekniska namnet kan inte ändras efter att dimensionen har skapats.",
        },
        localizedTitleHeader: {
          title: "Lokaliserade titlar",
          helpText:
            "Du kan ge dimensionen en titel på olika språk. Titeln behöver inte anges på alla språk som stöds: om titeln inte anges på det valda språket används standardspråket istället, och om det inte heller är inställt, det tekniska namnet.",
        },
        title: {
          fi: "Titeln på finska",
          en: "Titeln på engelska",
          sv: "Titeln på svenska",
        },
        isKeyDimension: {
          title: "Nyckeldimension",
          helpText: "Val för nyckeldimensionerna visas i svarslistan.",
        },
        isMultiValue: {
          title: "Flera val",
          helpText: "Om markerad kan flera värden väljas för denna dimension.",
        },
        isShownToSubject: {
          title: "Visas för respondenten",
          helpText:
            "Om detta är valt kommer värdena för denna dimension att visas för respondenten i den individuella svarsvyn i deras profil. Om den här dimensionen dessutom är en nyckeldimension kommer den att visas i profilsvarslistan.",
        },
      },
    },
    editValueModal: {
      editTitle: "Ändra val",
      addTitle: "Lägg till val",
      actions: {
        submit: "Spara val",
        cancel: "Avbryt",
      },
      attributes: {
        slug: {
          title: "Tekniskt namn",
          // TODO add pattern for slug and document it in helpText
          helpText:
            "Ett maskinläsbart, kort namn på en dimension. Det tekniska namnet kan inte ändras efter att dimensionen har skapats.",
        },
        color: UNSURE({
          title: "Färg",
          helpText:
            "Färgen på värdet i svarslistan. Använd ljusa färger: de kommer att ljusas upp eller mörkas efter behov.",
        }),
        isInitial: UNTRANSLATED({
          title: "Initial value",
          helpText: "If set, this value will be applied to all new responses.",
        }),
        localizedTitleHeader: {
          title: "Titel lokaliserad",
          helpText:
            "Du kan ge dimensionen en titel på olika språk. Titeln behöver inte anges på alla språk som stöds: om titeln inte anges på det valda språket används standardspråket istället, och om det inte heller är inställt, det tekniska namnet.",
        },
        title: {
          fi: "Titeln på finska",
          en: "Titeln på engelska",
          sv: "Titeln på svenska",
        },
      },
    },
    createSurveyModal: {
      title: "Skapa ny enkät",
      actions: {
        submit: "Skapa",
        cancel: "Avbryt",
      },
    },
    editSurveyPage: {
      title: "Ändra enkät",
      actions: {
        submit: "Spara fält",
      },
    },
  },

  SignInRequired: {
    metadata: {
      title: "Inloggning krävs – Kompassi",
    },
    title: "Inloggning krävs",
    message: "Du måste logga in för att visa den här sidan.",
    signIn: "Logga in",
  },

  Brand: {
    appName: (
      <>
        Kompassi<sup>v2 BETA</sup>
      </>
    ),
    plainAppName: "Kompassi",
  },

  LanguageSwitcher: {
    supportedLanguages: {
      fi: "finska",
      en: "engelska",
      sv: "svenska",
    },
    // NOTE: value always in target language
    switchTo: {
      fi: "Suomeksi",
      en: "In English",
      sv: "På svenska",
    },
  },
};

export default translations;
