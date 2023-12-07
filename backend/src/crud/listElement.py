import uuid

from sqlalchemy.orm import Session

from src.models.listElement import ListElement
from src.schemas.listElement import ListElementCreate, ListElementBase


def get_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ListElement).offset(skip).limit(limit).all()


def get_list(db: Session, id: uuid.UUID) :
    return db.query(ListElement).filter(ListElement.id == id).first()


def create_list(db: Session, list: ListElementCreate):
    db_list = ListElement(title = list.title)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


def update_list(db: Session, id: uuid.UUID, update: ListElementBase):
    db_list = db.query(ListElement).filter(ListElement.id == id).first()
    db_list.title = update.title
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


def delete_list(db:Session, id: uuid.UUID):
    db_list = db.query(ListElement).filter(ListElement.id == id).first()
    db.delete(db_list)
    db.commit()
    return 1
