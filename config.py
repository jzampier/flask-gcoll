"""Config Module"""
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
bd_user = os.getenv('user')
bd_passwd = os.getenv('passwd')
bd_host = os.getenv('host')
bd_port = int(os.getenv('port'))
secret_key = os.getenv('secret_key')
SECRET_KEY = secret_key
MYSQL_HOST = bd_host
MYSQL_USER = bd_user
MYSQL_PASSWORD = bd_passwd
MYSQL_DB = 'gamecollection'
MYSQL_PORT = bd_port
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
