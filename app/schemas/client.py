from pydantic import BaseModel


class ClientSchema(BaseModel):
    name: str
    social_status_id: int



class ClientAddSchema(ClientSchema):
    pass


class ClientGetSchema(ClientSchema):
    id:int
    pass

class ClientUpdateSchema(ClientGetSchema):
    pass