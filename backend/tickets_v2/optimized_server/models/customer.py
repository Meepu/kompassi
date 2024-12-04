import pydantic


class Customer(pydantic.BaseModel, frozen=True, populate_by_name=True):
    """
    Arbitrary limits on field lengths to prevent someone putting megabytes of
    hodgepodge in the DB.
    """

    first_name: str = pydantic.Field(
        validation_alias="firstName",
        serialization_alias="firstName",
        max_length=100,
    )
    last_name: str = pydantic.Field(
        validation_alias="lastName",
        serialization_alias="lastName",
        max_length=200,
    )
    email: pydantic.EmailStr = pydantic.Field(
        validation_alias="email",
        serialization_alias="email",
        max_length=300,
    )
    phone: str | None = pydantic.Field(
        validation_alias="phone",
        serialization_alias="phone",
        default=None,
        max_length=50,
    )

    # @pydantic.field_validator("phone", mode="before")
    # @staticmethod
    # def validate_phone(value: str | None) -> str | None:
    #     if value == "":
    #         return None
    #     return value
