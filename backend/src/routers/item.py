import uuid
from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.crud.item import get_items_by_list, get_item, create_item, update_item, delete_item
from src.database import SessionLocal
from src.schemas.listElement import ItemCreate, ItemSchema, ItemBase

router = APIRouter(prefix="/items", tags=["items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_description="Get all Items by List Id", response_model=List[ItemSchema])
async def get_items_by_list_id(list_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_items_by_list(list_id=list_id, db=db)


@router.get("/{id}", response_description="Get Item with id", response_model=ItemSchema)
async def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    if(db_item := get_item(id=id, db=db)) is not None:
        return db_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Item with ID {id} not found!"
    )

@router.post(
    "/",
    response_description="Create a new Item",
    status_code=status.HTTP_201_CREATED,
    response_model=ItemSchema
)
async def create(item: ItemCreate, db: Session = Depends(get_db)):
    if(created_item:=create_item(db=db, item=item)) is not None:
        return created_item
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Conflict while creating new item")


@router.put(
    "/{id}",
    response_description="Update an existing Item",
    status_code=status.HTTP_200_OK,
    response_model=ItemSchema
)
async def update(id: uuid.UUID, to_update_item: ItemBase, db: Session = Depends(get_db)):
    if(item := update_item(id=id, update=to_update_item, db=db)) is not None:
        return item
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while updating item  with ID {id}")


@router.delete(
    "/{id}",
    response_description="Delete a list",
    status_code=status.HTTP_200_OK,
)
async def delete(id: uuid.UUID, db:Session= Depends(get_db)):
    if delete_item(id=id, db=db) == 1:
        return f"Item with ID {id} was deleted"
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while deleting item with ID {id}")
