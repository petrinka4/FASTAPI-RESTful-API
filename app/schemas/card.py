from pydantic import BaseModel, validator


class CardSchema(BaseModel):
    balance: int
    account_id: int

    

class CardAddSchema(CardSchema):
    @validator('balance')
    def validate_balance(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Balance shouldnt be negative")
        return value


class CardGetSchema(CardSchema):
    id:int
    pass

class CardUpdateSchema(CardGetSchema):
    pass