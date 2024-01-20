"use client";

import type { ReactNode } from "react";
import { useFormStatus } from "react-dom";
import { Layout } from "./models";

interface SubmitButtonProps {
  layout?: Layout;
  children?: ReactNode;
}

export default function SubmitButton({ layout, children }: SubmitButtonProps) {
  const { pending } = useFormStatus();

  switch (layout) {
    case Layout.Horizontal:
      return (
        <div className="row mb-2">
          <div className="col-md-3"></div>
          <div className="col-md-9">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={pending}
            >
              {children}
            </button>
          </div>
        </div>
      );
    default:
      return (
        <button
          type="submit"
          className="btn btn-primary mb-2"
          disabled={pending}
        >
          {children}
        </button>
      );
  }
}
