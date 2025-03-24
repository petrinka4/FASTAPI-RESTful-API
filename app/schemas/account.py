from pydantic import BaseModel, validator


class AccountSchema(BaseModel):
    balance: int
    client_id: int
    bank_id: int


class AccountGetSchema(AccountSchema):
    id: int


class AccountAddSchema(AccountSchema):
    @validator('balance')
    def validate_balance(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Balance shouldnt be negative")
        return value

class AccountUpdateSchema(AccountGetSchema):
    pass