from lib.models import Dog
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    engine = create_engine('sqlite:///dogs.db')
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, dog):
    return dog

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(f'%{name}%')).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.like(f'%{id}%')).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(f'%{name}%'), Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    return dog