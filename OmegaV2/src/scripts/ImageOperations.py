from models.Anime import Anime
from models.Manga import Manga
from models.AnimeCharacter import AnimeCharacter
from typing import Union, Iterable
import scripts.Configuration as config
import requests


def load_images(items: Union[Iterable[Anime], Iterable[Manga], Iterable[AnimeCharacter]]):
    """
    Downloads images for given items
    :param items:
    :return:
    """
    try:
        remove_old_images()
        for item in items:
            get_image(item)
    except Exception as e:
        raise e


def remove_old_images(directory: str = None):
    """
    Removes not used images
    :param directory:
    """
    try:
        if directory:
            from os import listdir, remove
            from os import path
            images_dir = listdir(directory)
            jpg_files = [file for file in images_dir if file.endswith(".jpg")]
            for file in jpg_files:
                path_to_file = path.join(directory, file)
                remove(path_to_file)
        else:
            remove_old_images(f'{config.images_path}/Characters')
            remove_old_images(f'{config.images_path}/Items')
    except Exception as e:
        raise e


def get_image(item: Union[Anime, Manga, AnimeCharacter]):
    """
    Downloads image for given item
    :param item:
    """
    try:
        if isinstance(item, Anime) or isinstance(item, Manga):
            path = f'{config.images_path}/Items/{item.id}.jpg'
        else:
            path = f'{config.images_path}/Characters/{item.name}.jpg'
        response = requests.get(item.image)
        file = open(path, "wb")
        file.write(response.content)
        file.close()
    except Exception as e:
        raise e
