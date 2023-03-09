""" This file responsible for adding tables to database """
import os
import sys
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKeyConstraint, Date
script_dir = os.path.dirname(os.path.abspath(__file__))
connection_path = os.path.join(script_dir, '..', '..', 'connection.py')
sys.path.append(os.path.dirname(connection_path))

from connection import engine

metadata = MetaData()


def if_table_exist_in_database(table):
    """ This method responsible for checking if tables with certain names exist in database """
    metadata.reflect(bind=engine)

    if table in metadata.tables:
        return True
    return False


def upgrade():
    """ This method responsible for creating tables in database """

    if not if_table_exist_in_database(table='employer') and not if_table_exist_in_database(table='employee'):
        Table('employer', metadata,
              Column('id', Integer(), nullable=False, primary_key=True),
              Column('name', String(length=50), nullable=False),
              Column('lastname', String(length=50), nullable=False),
              Column('email', String(length=50), nullable=False),
              Column('date_of_birth', Date, nullable=False),
              )
        Table('employee', metadata,
              Column('id', Integer(), nullable=False, primary_key=True),
              Column('name', String(length=50), nullable=False),
              Column('lastname', String(length=50), nullable=False),
              Column('email', String(length=50), nullable=False),
              Column('date_of_birth', Date, nullable=False),
              Column('employer_id', Integer(), nullable=True),
              ForeignKeyConstraint(['employer_id'], ['employer.id'], ),
              )

        metadata.create_all(engine)
        return True

    return False


print(upgrade())
