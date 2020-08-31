from sqlalchemy import Column, Integer, String
from modules.db_config import Base, engine

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String(1024)) # Char limit of an embed field
    user = Column(Integer)
    timestamp = Column(String)

Base.metadata.create_all(engine)