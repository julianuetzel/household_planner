import uuid

from pydantic import BaseModel


class ItemBase(BaseModel):
    text: str
    status: int


class ItemCreate(ItemBase):
    list_id: uuid.UUID


class ItemSchema(ItemBase):
    id: uuid.UUID
    list_id: uuid.UUID

    class Config:
        orm_mode = True


class ListElementBase(BaseModel):
    title: str


class ListElementCreate(ListElementBase):
    pass


class ListElementSchema(ListElementBase):
    id: uuid.UUID
    items: list[ItemSchema] = []

    class Config:
        orm_mode = True
