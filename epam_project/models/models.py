from sqlalchemy import Table, Integer, String, \
    Column, ForeignKey, Boolean, DateTime, Date
from sqlalchemy.orm import relationship
from base import Base
from connection import engine


class Employer(Base):

    __tablename__ = 'employer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    date_of_birth = Column(Date)

    employees = relationship('Employee', backref='employer', lazy=True)

    def __init__(self, name, lastname, email, date_of_birth):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.date_of_birth = date_of_birth


class Employee(Base):

    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    date_of_birth = Column(Date)

    employer_id = Column(Integer, ForeignKey('employer.id'), nullable=False)

    def __init__(self, name, lastname, email, date_of_birth):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.date_of_birth = date_of_birth


Base.metadata.create_all(engine)