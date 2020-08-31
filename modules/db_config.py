import os

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASEDIR = os.path.abspath(os.path.dirname(__file__))
BASEDIR = os.path.dirname(BASEDIR)

if not os.path.isdir(os.path.join(BASEDIR, 'databases')):
    os.makedirs(os.path.join(BASEDIR, 'databases'))

engine = db.create_engine('sqlite:///' + os.path.join(BASEDIR, 'databases', 'notes.db'))
Base = declarative_base()
sessionmkr = sessionmaker(bind=engine)