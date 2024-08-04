from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

class database():
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = f"""postgresql://{
                os.environ("user")
            }:{
                os.environ("password")
            }@localhost/{
                os.environ("dbname")
            }"""
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()