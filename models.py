from sqlalchemy import Column, Integer, String
from db_config import Base, engine

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    user = Column(String)
    timestamp = Column(String)

Base.metadata.create_all(engine)