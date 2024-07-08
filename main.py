from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

app = FastAPI()

class Revenue(BaseModel):
    month: str
    revenue: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/revenues")
async def read_revenues(db:db_dependency):
    result = db.query(models.Revenue).all()
    if not result:
        raise HTTPException(status_code=404, detail='No revenues found.')
    return result

