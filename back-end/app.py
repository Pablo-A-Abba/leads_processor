from fastapi import FastAPI
from .routers import person

app = FastAPI()

app.include_router(person.router, prefix="/person", tags=["person"])

