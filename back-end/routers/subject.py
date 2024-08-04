from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import crud, models, schemas
from ..database import database

models.Base.metadata.create_all(bind=database.engine)

routerSubject = APIRouter()

@routerSubject.post("/create", response_model=schemas.PersonSubjectCreate)
def create_subject(subject: schemas.PersonSubjectCreate, db: Session = Depends(database.get_db)):
    return crud.SubjectCrud.create_subject(db=db, subject=subject)

@routerSubject.get("/list", response_model=List[schemas.PersonSubject])
def read_subject(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    subject = crud.SubjectCrud.get(db, skip=skip, limit=limit)
    return subject

