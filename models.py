from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class GuestbookEntry(db.Model):
    """Guest book entry model"""
    __tablename__ = 'guestbook'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Repr dunder method"""
        return f'GuestbookEntry from {self.name}'