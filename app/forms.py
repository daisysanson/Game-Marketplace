from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired()])
    date_released = DateField('Date Released', validators=[InputRequired("Please enter a date")],format='%d/%m/%Y')

    def validate_date(self, date):
        return date < date(1970, 1, 1)
