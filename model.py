from flask_sqlalchemy import SQLAlchemy


DEFAULT_IMG = "https://image.shutterstock.com/image-vector/orthography-signs-black-question-mark-260nw-1359319715.jpg"


db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True, nullable=False)


    def image_url(self):
        """wil return an image for the pet or use the deafult if not available"""

        return self.photo_url or DEFAULT_IMG
