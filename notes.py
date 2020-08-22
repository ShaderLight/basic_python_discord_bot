import models as md
from db_config import engine, sessionmkr, Base
from datetime import datetime

Base.metadata.create_all(engine)

class Notes:
    def __init__(self, engine, sessionmkr):
        self.engine = engine
        self.sessionmkr = sessionmkr

    def add_note(self, content, nickname):
        session = self.sessionmkr()

        timestamp = datetime.now()
        timestamp = timestamp.strftime('%d/%m/%Y %H:%M:%S')

        note = md.Note(content=content, nickname=nickname, timestamp=timestamp)

        session.add(note)
        session.commit()

    def search_by_id(self, id):
        session = self.sessionmkr()

        result = session.query(md.Note).filter(md.Note.id == id).one()

        return result

    def search_by_nickname(self, nickname):
        session = self.sessionmkr()

        results = session.query(md.Note).filter(md.Note.nickname == nickname).all()

        return results


note_manager = Notes(engine,sessionmkr)

note_manager.add_note('a', 'b')