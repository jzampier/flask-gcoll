from flask import Flask, render_template

app = Flask(__name__)


class Game:
    """_summary_"""

    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console


@app.route('/begining')
def hello():
    """_summary_

    Returns:
        _description_
    """
    game1 = Game('World of Warcraft', 'MMORPG', 'PC')
    game2 = Game('League of Legends', 'MOBA', 'PC')
    game3 = Game('Unreal Tournament', 'FPS', 'PC')
    game4 = Game('Street Fighter II', 'Fight', 'Arcade')
    game_list = [game1, game2, game3, game4]
    return render_template('index.html', ttl='my game collection', games=game_list)


app.run()
