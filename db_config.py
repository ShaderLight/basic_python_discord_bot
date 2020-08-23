import os

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASEDIR = os.path.abspath(os.path.dirname(__file__))
if not os.path.isdir(os.path.join(BASEDIR, 'databases')):
    os.makedirs(os.path.join(BASEDIR, 'databases'))

engine = db.create_engine('sqlite:///' + os.path.join(BASEDIR, 'databases', 'notes.db'))
Base = declarative_base()
sessionmkr = sessionmaker(bind=engine)