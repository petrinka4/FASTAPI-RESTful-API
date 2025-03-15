from pydantic import BaseModel, validator


class AccountAddSchema(BaseModel):
    balance: int
    client_id: int
    bank_id: int

    @validator('balance')
    def validate_balance(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Balance shouldnt be negative")
        return value
