import uuid

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.crud.listElement import get_lists, get_list, create_list, update_list, delete_list
from src.database import SessionLocal
from src.schemas.listElement import ListElementCreate, ListElementSchema

router = APIRouter(prefix="/lists", tags=["lists"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_description="Get all Lists", response_model=list[ListElementSchema])
async def get_all(db: Session = Depends(get_db)):
    return get_lists(db)



@router.get("/{id}", response_description="Get List with id", response_model=ListElementSchema)
async def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    if(db_list := get_list(id=id, db=db)) is not None:
        return db_list
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"list with ID {id} not found!"
    )

@router.post(
    "/",
    response_description="Create a new list",
    status_code=status.HTTP_201_CREATED,
    response_model=ListElementSchema)
async def create(list: ListElementCreate, db: Session = Depends(get_db)):
    if(created_list:=create_list(db=db, list=list)) is not None:
        return created_list
    raise HTTPException(status_code=409, detail="Conflict while creating new list")


@router.put(
    "/{id}",
    response_description="Update an existing Item",
    status_code=status.HTTP_200_OK,
    response_model=ListElementSchema
)
async def update(id: uuid.UUID, to_update_item: ListElementSchema, db: Session = Depends(get_db)):
    if(listElement := update_list(id=id, update=to_update_item, db=db)) is not None:
        return listElement
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while updating list with ID {id}")


@router.delete(
    "/{id}",
    response_description="Delete a list",
    status_code=status.HTTP_200_OK,
)
async def delete(id: uuid.UUID, db:Session= Depends(get_db)):
    if delete_list(id=id, db=db) == 1:
        return f"List with ID {id} was deleted"
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while deleting list with ID {id}")
