import uuid
from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.crud.note import get_notes, get_note, create_note, update_note, delete_note
from src.database import SessionLocal
from src.schemas.note import NoteCreate, NoteSchema, NoteBase

router = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_description="Get all Notes", response_model=List[NoteSchema])
async def get_all(db: Session = Depends(get_db)):
    return get_notes(db=db)


@router.get("/{id}", response_description="Get Item with id", response_model=NoteSchema)
async def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    if(db_item := get_note(id=id, db=db)) is not None:
        return db_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Note with ID {id} not found!"
    )

@router.post(
    "/",
    response_description="Create a new Note",
    status_code=status.HTTP_201_CREATED,
    response_model=NoteSchema)
async def create(note: NoteCreate, db: Session = Depends(get_db)):
    if(created_item:=create_note(db=db, note=note)) is not None:
        return created_item
    raise HTTPException(status_code=409, detail="Conflict while creating new note")


@router.put(
    "/{id}",
    response_description="Update an existing Item",
    status_code=status.HTTP_200_OK,
    response_model=NoteSchema
)
async def update(id: uuid.UUID, to_update_note: NoteBase, db: Session = Depends(get_db)):
    if(note := update_note(id=id, update=to_update_note, db=db)) is not None:
        return note
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while updating note with ID {id}")


@router.delete(
    "/{id}",
    response_description="Delete a list",
    status_code=status.HTTP_200_OK,
)
async def delete(id: uuid.UUID, db:Session= Depends(get_db)):
    if delete_note(id=id, db=db) == 1:
        return f"Note with ID {id} was deleted"
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conflict while deleting note with ID {id}")
