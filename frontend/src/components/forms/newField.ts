import { Field, FieldType } from "./models";
import generateUniqueIdentifier from "@/helpers/generateUniqueIdentifier";

export default function newField(
  type: FieldType,
  usedIdentifiers: string[],
): Field {
  const slug = generateUniqueIdentifier(type, usedIdentifiers);
  switch (type) {
    case "Divider":
    case "Spacer":
    case "StaticText":
    case "SingleLineText":
    case "MultiLineText":
    case "NumberField":
    case "DecimalField":
    case "SingleCheckbox":
      return { type, slug, title: "" };
    case "SingleSelect":
    case "MultiSelect":
      return { type, slug, title: "", choices: [] };
    case "RadioMatrix":
      return { type, slug, title: "", choices: [], questions: [] };
  }

  throw new Error("Unknown field type");
}
