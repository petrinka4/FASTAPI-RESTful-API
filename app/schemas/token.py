from pydantic import BaseModel


class TokenInfo(BaseModel):
    access_token:str
    refresh_token:str|None=None
    token_type:str

class AccessTokenPayloadSchema(BaseModel):
    type:str="access"
    sub:str
    username:str
    role:str

class RefreshTokenPayloadSchema(BaseModel):
    type:str="refresh"
    sub:str
    username:str

