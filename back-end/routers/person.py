from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import crud, models, schemas
from ..database import database

models.Base.metadata.create_all(bind=database.engine)

routerPerson = APIRouter()

@routerPerson.post("/create", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(database.get_db)):
    return crud.PersonCrud.create_person(db=db, person=person)

@routerPerson.get("/list", response_model=List[schemas.Person])
def read_people(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    people = crud.PersonCrud.get_people(db, skip=skip, limit=limit)
    return people

@routerPerson.get("/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(database.get_db)):
    db_person = crud.PersonCrud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person
