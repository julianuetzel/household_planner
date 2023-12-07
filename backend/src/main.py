import uvicorn
from fastapi import FastAPI
from routers.listElement import router as listRouter
from routers.item import router as itemRouter
from routers.note import router as noteRouter
from src.database import engine
from src.models.note import Base

app = FastAPI()

app.include_router(listRouter)
app.include_router(itemRouter)
app.include_router(noteRouter)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=5000)