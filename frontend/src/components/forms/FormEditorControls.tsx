"use client";

import Button from "react-bootstrap/Button";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import ButtonToolbar from "react-bootstrap/ButtonToolbar";
import Stack from "react-bootstrap/Stack";

import AddFieldDropdown from "./AddFieldDropdown";
import {
  canEditField,
  canMoveDown,
  canMoveUp,
  moveDown,
  moveUp,
} from "./formEditorLogic";
import { Field, FieldType } from "./models";

import "./FormEditor.scss";
import type { Translations } from "@/translations/en";

interface FormEditorControlsProps {
  value: Field[];
  field: Field;
  onChange(fields: Field[]): void;
  onAddField(fieldType: FieldType, aboveFieldName: string): void;
  onRemoveField(fieldName: string): void;
  onEditField(fieldName: string): void;
  messages: Translations["FormEditor"];
}

const FormEditorControls = ({
  value: fields,
  field,
  onAddField,
  onChange,
  onRemoveField,
  onEditField,
  messages,
}: FormEditorControlsProps) => {
  return (
    <ButtonToolbar className="mt-1">
      <Stack direction="horizontal" gap={2}>
        <ButtonGroup>
          <AddFieldDropdown
            title={messages.addFieldAbove + "…"}
            onSelect={(fieldType) => onAddField(fieldType, field.slug)}
            messages={messages}
          />
        </ButtonGroup>
        <ButtonGroup>
          <Button
            size="sm"
            onClick={() => onChange(moveUp(fields, field.slug))}
            variant="outline-secondary"
            disabled={!canMoveUp(fields, field.slug)}
          >
            {messages.moveUp}
          </Button>
          <Button
            size="sm"
            onClick={() => onChange(moveDown(fields, field.slug))}
            variant="outline-secondary"
            disabled={!canMoveDown(fields, field.slug)}
          >
            {messages.moveDown}
          </Button>
        </ButtonGroup>
        <ButtonGroup>
          <Button
            size="sm"
            onClick={() => onEditField(field.slug)}
            disabled={!canEditField(field)}
            variant="outline-secondary"
          >
            {messages.editField}…
          </Button>
          <Button
            size="sm"
            onClick={() => onRemoveField(field.slug)}
            variant="outline-danger"
          >
            {messages.removeField}…
          </Button>
        </ButtonGroup>
      </Stack>
    </ButtonToolbar>
  );
};

export default FormEditorControls;
