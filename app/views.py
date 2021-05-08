from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Games
from app.forms import InputForm
from app.sort import add_games_to_array
import logging



@app.route('/')
def index():
    return render_template("home.html")

@app.route('/show_games')
def show_games():
    games = db.session.query(Games).all()
    sorted_games = add_games_to_array(games)
    print(sorted_games)
    return render_template('show_games.html', sorted_games=sorted_games)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    input_form = InputForm()
    game = Games.query.filter_by(id=id).first()
    if request.method == "POST":
        if input_form.validate_on_submit():
            Games.query.filter_by(id=id).delete()

            name = input_form.name.data
            rating = input_form.rating.data
            date_released = input_form.date_released.data  
           
            game= Games(name, rating, date_released)
            db.session.add(game)
            db.session.commit()
            return redirect('/show_games')

    flash_errors(input_form)
    return render_template('update.html', game=game, form=input_form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == "POST":
        games = db.session.query(Games).all()
        game_to_delete = Games.query.get_or_404(id)
    
        Games.query.filter_by(id=id).delete()
        db.session.commit()
        flash('Game successfully deleted')
        return redirect('/show_games')
    
    return render_template("show_games.html")
    

 
@app.route('/add_game', methods=['POST', 'GET'])
def add_game():
    input_form = InputForm()

    if request.method == "POST":
        if input_form.validate_on_submit():

            name = input_form.name.data
            rating = input_form.rating.data
            date_released = input_form.date_released.data


            new_game = Games(name, rating, date_released)
            db.session.add(new_game)
            db.session.commit()
            logging.info('Game Added')
            
            flash('Game successfully added')
            return redirect(url_for('show_games'))


    flash_errors(input_form)
    return render_template('add_game.html', form=input_form)
        

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.template_filter('strftime')
def _jinja2_filter_datetime(date):

    return date.strftime('%d/%m/%Y')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
    

