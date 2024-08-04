from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for Person and Degree
person_degree_association = Table(
    'person_degree', Base.metadata,
    Column('person_id', Integer, ForeignKey('people.id'), primary_key=True),
    Column('degree_id', Integer, ForeignKey('degrees.id'), primary_key=True)
)

# Association table to hold the subject and grade relationship
class PersonSubject(Base):
    __tablename__ = 'person_subject'
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), primary_key=True)
    grade = Column(Integer)

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    telephone = Column(String, index=True)
    university = Column(String, index=True)
    degrees = relationship("Degree", secondary=person_degree_association, back_populates="people")
    subjects = relationship("PersonSubject", back_populates="person", cascade="all, delete-orphan")

class Degree(Base):
    __tablename__ = "degrees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    field = Column(String, index=True)
    people = relationship("Person", secondary=person_degree_association, back_populates="degrees")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    people = relationship("PersonSubject", back_populates="subject", cascade="all, delete-orphan")

PersonSubject.person = relationship("Person", back_populates="subjects")
PersonSubject.subject = relationship("Subject", back_populates="people")
