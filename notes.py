import models as md
from datetime import datetime
from db_config import sessionmkr

class Notes:
    def __init__(self):
        pass

    def add_note(self, content, nickname):
        session = sessionmkr()

        timestamp = datetime.now()
        timestamp = timestamp.strftime('%d/%m/%Y %H:%M:%S')

        note = md.Note(content=content, nickname=nickname, timestamp=timestamp)

        session.add(note)
        session.commit()
        session.close()

    def search_by_id(self, id):
        session = sessionmkr()

        result = session.query(md.Note).filter(md.Note.id == id).one()

        session.close()
        return result

    def search_by_nickname(self, nickname):
        session = sessionmkr()

        results = session.query(md.Note).filter(md.Note.nickname == nickname).all()

        session.close()
        return results