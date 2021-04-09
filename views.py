from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, Blueprint
from main import app
from werkzeug.utils import redirect
from datetime import datetime
from models import Games
from time import strftime
# from dateutil.parser import *

db = Games
# my_view= Blueprint('my_view', __name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    game_to_update = Games.query.get_or_404(id)
    if request.method == "POST":
        game_to_update.name = request.form['name']
        game_to_update.rating = request.form['rating']
    
        try:
            db.session.commit()
            return redirect('/games')
        except:
            return "There was a problem updating the game"
    else:
        return render_template('update.html', game_to_update=game_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    game_to_delete = Games.query.get_or_404(id)
    try:
        db.session.delete(game_to_delete)
        db.session.commit()
        return redirect('/games')
    except:
        return "There was a problem deleteing the game"
    else:
        return render_template('delete.html', game_to_delete)

@app.route('/games', methods=['POST', 'GET'])
def games():
    if request.method == "POST":
        game_name = request.form['name']
        rating = request.form['rating']
        date_released = request.form['date_released']
        new_game = Games(name=game_name, rating=rating, date_released=date_released)
        try:  #push to our database
            db.session.add(new_game)
            db.session.commit()
            return redirect('/games')
        except:
            return "there was an error adding this game"
    else:
        list_of_games = Games.query.order_by(Games.name)
        return render_template("games.html", games=list_of_games)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.template_filter('strftime')
def _jinja2_filter_datetime(date):

    return date.strftime('%d-%m-%Y')


    
def validator(rating):
    rating_int = int(rating)
    if rating_int < 0 | rating_int > 5:
        print("False")
        return False 
    else:
        print("True")
        return True
