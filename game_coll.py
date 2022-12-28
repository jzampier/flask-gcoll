"""Flask Game Site"""
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'tio_julio'


class Game:
    """Class with our game atributes"""

    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console


game1 = Game('World of Warcraft', 'MMORPG', 'PC')
game2 = Game('League of Legends', 'MOBA', 'PC')
game3 = Game('Unreal Tournament', 'FPS', 'PC')
game4 = Game('Street Fighter II', 'Fight', 'Arcade')
game_list = [
    game1,
    game2,
    game3,
    game4,
]


@app.route('/')
def index():
    """Render homepage

    Returns:
        Render index.html page
    """
    return render_template('index.html', ttl='my game collection', games=game_list)


@app.route('/new_game')
def new():
    """Render the new game page"""
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
    game_list.append(game)
    return redirect('/')


@app.route('/login')
def login():
    """render login page

    Returns:
        renders our login page
    """
    return render_template('login.html')


@app.route(
    '/authenticate',
    methods=[
        'POST',
    ],
)
def authenticate():
    """Authenticates user and redirects to home page
    or login page (if password is incorrect)"""
    if 'master' == request.form.get('user_password'):
        session['user_authenticated'] = request.form.get('user_name')
        flash(request.form.get('user_name') + ' has successfully logged in')
        return redirect('/')
    flash('Loggin attemept failed! Type your password correctly')
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
