"""Defines what data is expected from the client and the server."""

from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str


class URL(URLBase):
    clicks: int
    is_active: bool

    class Config:
        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
