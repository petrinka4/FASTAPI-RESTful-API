from pydantic import BaseModel


class ClientAddSchema(BaseModel):
    name: str
    social_status_id: int
