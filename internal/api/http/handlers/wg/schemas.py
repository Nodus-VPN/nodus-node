from pydantic import BaseModel


class CreateWGClientRequest(BaseModel):
    client_address: str
