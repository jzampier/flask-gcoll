"""Classes and methods to CRUD operations"""
from game_coll import User, Game

SQL_DELETE_GAME = 'DELETE from game where id = %s'
SQL_GAME_POR_ID = 'SELECT id, name, category, console from game where id = %s'
SQL_USER_POR_ID = 'SELECT id, name, senha from user where id = %s'
SQL_UPDATE_GAME = 'UPDATE game SET name=%s, category=%s, console=%s where id = %s'
SQL_SEARCH_GAMES = 'SELECT id, name, category, console from game'
SQL_CREATE_GAME = 'INSERT into game (name, category, console) values (%s, %s, %s)'


class GameDao:
    def __init__(self, db):
        self.__db = db

    def save(self, game):
        cursor = self.__db.connection.cursor()

        if game.game_id:
            cursor.execute(
                SQL_UPDATE_GAME, (game.name, game.category, game.console, game.game_id)
            )
        else:
            cursor.execute(SQL_CREATE_GAME, (game.name, game.category, game.console))
            game.game_id = cursor.lastrowid
        self.__db.connection.commit()
        return game

    def list(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SEARCH_GAMES)
        games = translate_games(cursor.fetchall())
        return games

    def search_for_id(self, game_id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_GAME_POR_ID, (game_id,))
        tupla = cursor.fetchone()
        return Game(tupla[1], tupla[2], tupla[3])

    def delete(self, game_id):
        self.__db.connection.cursor().execute(SQL_DELETE_GAME, (game_id,))
        self.__db.connection.commit()


class UserDao:
    def __init__(self, db):
        self.__db = db

    def search_for_id(self, user_id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USER_POR_ID, (user_id,))
        data = cursor.fetchone()
        user = translate_user(data) if data else None
        return user


def translate_games(games):
    def create_games_w_tuple(tupla):
        return Game(tupla[1], tupla[2], tupla[3])

    return list(map(create_games_w_tuple, games))


def translate_user(tupla):
    return User(tupla[0], tupla[1], tupla[2])
