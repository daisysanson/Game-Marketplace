
from datetime import datetime
from main import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer(), nullable=False) 
    date_released = db.Column(db.DateTime, default=datetime)

    def __repr__(self):
        return '<Game %r>' % self.id
