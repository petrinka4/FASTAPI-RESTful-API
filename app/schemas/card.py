from pydantic import BaseModel, validator


class CardAddSchema(BaseModel):
    balance: int
    account_id: int

    @validator('balance')
    def validate_balance(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Balance shoudnt be negative")
        return value
