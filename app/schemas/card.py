from pydantic import BaseModel, validator


class CardSchema(BaseModel):
    account_id: int

    

class CardAddSchema(CardSchema):
    pass


class CardGetSchema(CardSchema):
    id:int
    balance: int
    pass

class CardUpdateSchema(CardSchema):
    balance: int
    @validator('balance')
    def validate_balance(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Balance shouldnt be negative")
        return value
    pass