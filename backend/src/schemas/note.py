import uuid

from pydantic import BaseModel


class NoteBase(BaseModel):
    text: str


class NoteCreate(NoteBase):
    pass


class NoteSchema(NoteBase):
    id: uuid.UUID

    class Config:
        orm_mode = True