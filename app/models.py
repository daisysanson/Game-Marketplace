
from datetime import datetime, date
from app import db



class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer(), nullable=False) 
    date_released = db.Column(db.Date(), default=date)

    def __init__(self, name,rating,date_released):
        self.name = name
        self.rating = rating
        self.date_released = date_released

    def __repr__(self):
        return '<Game %r>' % self.id
