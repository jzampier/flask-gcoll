"""Helpers methods"""
import os
from game_coll import app


def retrieve_img(game_id):
    """Retrieves an image without needing timestamp information"""
    for file_name in os.listdir(app.config.get('UPLOAD_PATH')):
        if f'img{game_id}' in file_name:
            return file_name


def delete_img(game_id):
    """Delete images"""
    file = retrieve_img(game_id)
    os.remove(os.path.join(app.config.get('UPLOAD_PATH'), file))
