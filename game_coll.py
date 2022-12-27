"""Flask Game Site"""
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Game:
    """_summary_"""

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
    """_summary_

    Returns:
        _description_
    """
    return render_template('index.html', ttl='my game collection', games=game_list)


@app.route('/new_game')
def new():
    """_summary_"""
    return render_template('new_game.html', ttl='New Game')


@app.route(
    '/create',
    methods=[
        'POST',
    ],
)
def create():
    """_summary_"""
    name = request.form.get('name')
    category = request.form.get('category')
    console = request.form.get('console')
    game = Game(name, category, console)
    game_list.append(game)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

#!4.6
