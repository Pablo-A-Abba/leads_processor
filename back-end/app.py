from fastapi import FastAPI
from .routers import person,subject

app = FastAPI()


app.include_router(person.routerPerson, prefix="/person", tags=["person"])
app.include_router(subject.routerSubject, prefix="/subject", tags=["person"])

