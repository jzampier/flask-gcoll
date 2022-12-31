"""Flask Game Site"""
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'tio_julio'


class Game:
    """Class with our game atributes"""

    def __init__(self, name, category, console, game_id=None) -> None:
        self.game_id = game_id
        self.name = name
        self.category = category
        self.console = console


class User:
    """New user class"""

    def __init__(self, user_id, user_name, user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password


user1 = User('julio', 'Julio Zampier', '1234')
user2 = User('fulano', 'Fulano de Tal', '4321')
user3 = User('Sikrano', 'Sikrano de Golveia', '5678')
users = {user1.user_id: user1, user2.user_id: user2, user3.user_id: user3}

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
    game_list.append(game)
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
    if request.form.get('user_name') in users:
        user = users[request.form.get('user_name')]
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
