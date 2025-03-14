from pydantic import BaseModel


class GetCaptionResponse(BaseModel):
    caption: str
