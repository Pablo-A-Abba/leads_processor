from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

router = APIRouter()


class Subject(BaseModel):
    name: str
    code: str
    note: float

class Degree(BaseModel):
    name: str
    field: str
    subject: list[Subject]

class Person(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    address: str
    telephone: str
    degree: List[Degree]

items = []

@router.post("/", response_model=Person)
def create_item(item: Item):
    items.append(item)
    return item

@router.get("/", response_model=List[Item])
def read_items():
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id >= len(items) or item_id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]