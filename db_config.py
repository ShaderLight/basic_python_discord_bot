import os

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

engine = db.create_engine('sqlite:///' + os.path.join(basedir, 'notes.db'))
Base = declarative_base()
sessionmkr = sessionmaker(bind=engine)