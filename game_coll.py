"""Flask Game Site"""
import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL

from dao import GameDao, UserDao
from models import Game, User

app = Flask(__name__)
app.secret_key = 'tio_julio'

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
bd_user = os.getenv('user')
bd_passwd = os.getenv('passwd')
bd_host = os.getenv('host')
bd_port = int(os.getenv('port'))

app.config['MYSQL_HOST'] = bd_host
app.config['MYSQL_USER'] = bd_user
app.config['MYSQL_PASSWORD'] = bd_passwd
app.config['MYSQL_DB'] = 'gamecollection'
app.config['MYSQL_PORT'] = bd_port

db = MySQL(app)

user_dao = UserDao(db)
game_dao = GameDao(db)


@app.route('/')
def index():
    """Render homepage

    Returns:
        Render index.html page
    """
    game_list = game_dao.list()
    return render_template('index.html', ttl='my game collection', games=game_list)


@app.route('/new')
def new():
    """Render the new game page"""
    if 'user_authenticated' not in session or session.get('user_authenticated') is None:
        #!using querystring to redirect to new_game after authentication
        return redirect(url_for('login', next_page=url_for('new')))
    return render_template('new_game.html', ttl='New Game')


@app.route(
    '/create',
    methods=[
        'POST',
    ],
)
def create():
    """Get information on field, append it to game_list
    and redirect to home page (/)"""
    name = request.form.get('name')
    category = request.form.get('category')
    console = request.form.get('console')
    game = Game(name, category, console)
    game_dao.save(game)
    return redirect(url_for('index'))


@app.route('/update/<int:game_id>')
def update(game_id):
    """Render the update page"""
    if 'user_authenticated' not in session or session.get('user_authenticated') is None:
        #!using querystring to redirect to new_game after authentication
        return redirect(url_for('login', next_page=url_for('update')))
    game = game_dao.search_for_id(game_id)
    return render_template('update.html', ttl='Update Game Info', game=game)


@app.route(
    '/edit',
    methods=[
        'POST',
    ],
)
def edit():
    """Get information on fields"""
    name = request.form.get('name')
    category = request.form.get('category')
    console = request.form.get('console')
    game = Game(name, category, console, game_id=request.form.get('game_id'))
    game_dao.save(game)
    return redirect(url_for('index'))


@app.route('/delete/<int:game_id>')
def delete(game_id):
    """delete a game from our database"""
    game_dao.delete(game_id)
    flash('Game deleted successfully.')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    """render login page

    Returns:
        renders our login page
    """
    # ? get information from querystring request.args.get(key)
    next_page = request.args.get('next_page')
    return render_template('login.html', next_page=next_page)


@app.route(
    '/authenticate',
    methods=[
        'POST',
    ],
)
def authenticate():
    """Authenticates user and redirects to home page
    or login page (if password is incorrect)"""
    user = user_dao.search_for_id(request.form.get('user_name'))
    if user:
        if user.user_password == request.form.get('user_password'):
            # Store user in session if password is correct
            session['user_authenticated'] = user.user_id
            # Message, if user's password is correct
            flash(user.user_name + ' has successfully logged in')
            #!Get page that user wants to access and asked for login
            next_page = request.form.get('next_page')
            return redirect(next_page)  # Store user in session if password is correct
    # Error message if password is incorrect
    flash('Loggin attemept failed! Type your password correctly')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """ "Logs out from our active session and redirects to home"""
    session['user_authenticated'] = None
    flash('No user are logged')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
