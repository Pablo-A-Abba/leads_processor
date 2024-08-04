from sqlalchemy.orm import Session
from . import models, schemas

class PersonCrud():
    def create_person(db: Session, person: schemas.PersonCreate):
        db_person = models.Person(
            first_name=person.first_name,
            last_name=person.last_name,
            email=person.email,
            address=person.address,
            telephone=person.telephone,
            university=person.university
        )
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        
        # Add degrees
        for degree_id in person.degrees:
            db_degree = db.query(models.Degree).filter(models.Degree.id == degree_id).first()
            if db_degree:
                db_person.degrees.append(db_degree)
        
        # Add subjects with grades
        for subject in person.subjects:
            db_person_subject = models.PersonSubject(
                person_id=db_person.id, 
                subject_id=subject.subject_id, 
                grade=subject.grade
            )
            db.add(db_person_subject)
        
        db.commit()
        db.refresh(db_person)
        return db_person

    def get_person(db: Session, person_id: int):
        return db.query(models.Person).filter(models.Person.id == person_id).first()

    def get_people(db: Session, skip: int = 0, limit: int = 10):
        return db.query(models.Person).offset(skip).limit(limit).all()

class SubjectCrud():
    def create_subject(db: Session, subject: schemas.PersonSubject):
        db_person_subject = models.PersonSubject(
            person_id=subject.person_id, 
            subject_id=subject.subject_id, 
            grade=subject.grade
        )
        db.add(db_person_subject)
        
        db.commit()
        db.refresh(db_person_subject)
        return db_person_subject

    def get_subjects(db: Session, person_id: int, skip: int = 0, limit: int = 10):
        return db.query(models.PersonSubject) \
                .filter(models.PersonSubject.person_id == person_id) \
                .offset(skip).limit(limit).all()
