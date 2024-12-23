interface Props {
  children?: React.ReactNode;
}

export default function ViewHeading({ children }: Props) {
  return <h1 className="mb-3">{children}</h1>;
}

ViewHeading.Sub = function Sub({ children }: Props) {
  return (
    <>
      {" "}
      <span className="fs-5 text-muted d-inline-block">{children}</span>
    </>
  );
};

export function ViewHeadingActionsWrapper({ children }: Props) {
  return (
    <div className={`d-flex justify-content-between align-items-center`}>
      {children}
    </div>
  );
}

export function ViewHeadingActions({ children }: Props) {
  return <div className="ms-auto">{children}</div>;
}
