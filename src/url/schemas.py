from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    target_url: HttpUrl


class URLInfo(URLBase):
    url: str