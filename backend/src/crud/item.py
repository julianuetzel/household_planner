import uuid

from sqlalchemy.orm import Session

from src.models.listElement import Item
from src.schemas.listElement import ItemCreate, ItemBase


def get_items_by_list(db: Session, list_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(Item).filter(Item.list_id == list_id).offset(skip).limit(limit).all()


def get_item(db: Session, id: uuid.UUID) :
    return db.query(Item).filter(Item.id == id).first()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(text = item.text, status = item.status, list_id = item.list_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, id: uuid.UUID, update: ItemBase):
    db_item = db.query(Item).filter(Item.id == id).first()
    db_item.text = update.text
    db_item.status = update.status
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db:Session, id: uuid.UUID):
    db_item = db.query(Item).filter(Item.id == id).first()
    db.delete(db_item)
    db.commit()
    return 1