from typing import List, Optional
from pydantic import BaseModel, EmailStr

class DegreeBase(BaseModel):
    name: str
    field: str

class DegreeCreate(DegreeBase):
    pass

class Degree(DegreeBase):
    id: int

    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    name: str
    code: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode = True

class PersonSubjectBase(BaseModel):
    subject_id: int
    grade: int

class PersonSubjectCreate(PersonSubjectBase):
    pass

class PersonSubject(PersonSubjectBase):
    person_id: int
    subject_id: int

    class Config:
        orm_mode = True

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    address: str
    telephone: str
    university: str

class PersonCreate(PersonBase):
    degrees: List[int] = []
    subjects: List[PersonSubjectCreate] = []

class Person(PersonBase):
    id: int
    degrees: List[Degree] = []
    subjects: List[PersonSubject] = []

    class Config:
        orm_mode = True
