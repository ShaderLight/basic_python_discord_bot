from sqlalchemy import Column, Integer, String
from db_config import Base

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    nickname = Column(String)
    timestamp = Column(String)
