"""Prepares our database"""
import os
import MySQLdb
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
bd_user = os.getenv('user')
bd_passwd = os.getenv('passwd')
bd_host = os.getenv('host')
bd_port = int(os.getenv('port'))

print('Connecting...')
conn = MySQLdb.connect(user=bd_user, passwd=bd_passwd, host=bd_host, port=bd_port)

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `gamecollection`;")
# conn.commit()

CREATE_TABLES = '''SET NAMES utf8;
    CREATE DATABASE `gamecollection` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `gamecollection`;
    CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `psw` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(CREATE_TABLES)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
    'INSERT INTO gamecollection.user (id, name, psw) VALUES (%s, %s, %s)',
    [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas'),
        ('julio', 'Julio Zampier', '1234'),
    ],
)

cursor.execute('select * from gamecollection.user')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo games
cursor.executemany(
    'INSERT INTO gamecollection.game (name, category, console) VALUES (%s, %s, %s)',
    [
        ('God of War 4', 'Action', 'PS4'),
        ('NBA 2k18', 'Sports', 'Xbox One'),
        ('Rayman Legends', 'Indie', 'PS4'),
        ('Super Mario RPG', 'RPG', 'SNES'),
        ('Super Mario Kart', 'Race', 'SNES'),
        ('Fire Emblem Echoes', 'Strategy', '3DS'),
    ],
)

cursor.execute('select * from gamecollection.game')
print(' -------------  games:  -------------')
for game in cursor.fetchall():
    print(game[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
