"""Models"""


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
