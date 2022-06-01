import json
import os
import pathlib
import sys
from PyQt5 import QtWidgets
from Windows.ErrorWindow import ErrorWindow


def _default_config() -> dict:
    """
    Default config
    :return: dict default config
    """
    cfg = {
        "DB_SERVER_IP": "IP",
        "DATABASE_NAME": "DATABASE_NAME",
        "DB_DRIVER": "SQL Server Native Client 11.0",
        "DB_USERNAME": "DATABASE_USERNAME",
        "DB_PASSWORD": "DATABASE_PASSWORD",
        "IMAGES_PATH": "./images"
    }
    return cfg


def load_cfg() -> dict:
    """
    Loads config from file
    If config does not exist, creates new
    :return: dict config
    """
    if not os.path.exists('./config/config.json'):
        os.makedirs('./config', exist_ok=True)
        with open('./config/config.json', 'w') as file:
            json.dump(_default_config(), file, indent=True)
    with open('./config/config.json', 'r') as file:
        return json.load(file)


# Loads config
try:
    _configuration = load_cfg()
    database_ip = _configuration['DB_SERVER_IP']
    database_name = _configuration['DATABASE_NAME']
    database_login = _configuration['DB_USERNAME']
    database_password = _configuration['DB_PASSWORD']
    database_driver = _configuration['DB_DRIVER']
    images_path = _configuration['IMAGES_PATH']
    # Checks if all necessary directories exists
    # If not creates them
    if not os.path.exists(images_path):
        os.mkdir(images_path)
        os.mkdir(f'{images_path}/Characters')
        os.mkdir(f'{images_path}/Items')
    if not os.path.exists(f'{images_path}/Characters'):
        os.mkdir(f'{images_path}/Characters')
    if not os.path.exists(f'{images_path}/Items'):
        os.mkdir(f'{images_path}/Items')
except Exception as e:
    print(e)
    app = QtWidgets.QApplication(sys.argv)
    err = ErrorWindow(sys.exc_info())
    sys.exit(app.exec_())
