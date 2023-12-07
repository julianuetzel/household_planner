import uuid

from sqlalchemy.orm import Session

from ..models.note import Note
from ..schemas.note import NoteCreate, NoteBase


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()


def get_note(db: Session, id: uuid.UUID) :
    return db.query(Note).filter(Note.id == id).first()


def create_note(db: Session, note: NoteCreate):
    db_note = Note(text = note.text)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, id: uuid.UUID, update: NoteBase):
    db_note = db.query(Note).filter(Note.id == id).first()
    db_note.text = update.text
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db:Session, id: uuid.UUID):
    db_note = db.query(Note).filter(Note.id == id).first()
    db.delete(db_note)
    db.commit()
    return 1
