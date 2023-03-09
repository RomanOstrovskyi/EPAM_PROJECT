"""Connection file where app, metadata, engine, session, db and migrate are defined"""
from flask import Flask
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from config import USERNAME, PORT, SERVER, DB
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

DATABASE_URL = os.environ['DATABASE_URL']

metadata = MetaData()
engine = create_engine(DATABASE_URL)
session = Session(bind=engine)

app = Flask(__name__, template_folder="EPAM_PROJECT/templates")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
