import os
import pickle
import json
import csv
import traceback
import xml.etree.cElementTree as ET
from datetime import datetime

__author__ = 'Maksym Kuzma C4a'

default_config = {
    'Language': 'English',
    'Encoding': 'utf-8',
    'Data path': './data.dat',
    'Export path': './export.csv',
    'Error path': './error.log'
}
config_path = 'cfg.json'  # Path to json config
current_config = {}       # Used to store loaded from file json config


def export_person(name: str, lastname: str, job: str, phone_number: int):
    """
    Exports input data as list into binary file
    :param name: Person name
    :param lastname: Person lastname
    :param job: Person job
    :param phone_number: Person phone number
    """
    with open(current_config['Data path'], 'ab') as file:
        pickle.dump([name, lastname, job, phone_number], file)


def load_data() -> list[list]:
    """
    Loads data from binary file
    :return: list of persons
    """
    with open(current_config['Data path'], 'rb') as file:
        person_list = []
        try:
            while True:
                person = pickle.load(file)
                person_list.append(person)
        except EOFError:
            return person_list


def create_config():
    """
    Creates default json config file
    """
    with open(config_path, 'w') as file:
        json.dump(default_config, file, indent=True)


def load_config():
    """
    Loads json config from file and sets current_config from loaded file
    """
    global current_config
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            current_config = json.load(file)
    else:
        create_config()
        current_config = default_config


def save_changes_to_config(lang: str, enc: str, data_path: str, export_path: str, error_path: str):
    """
    Saves changes to current json config
    :param lang: Language
    :param enc: Encryption
    :param data_path: Path to data.dat file
    :param export_path: Path to export.csv file
    :param error_path: Path to error.log file
    """
    with open(config_path, 'w') as file:
        current_config['Language'] = lang
        current_config['Encoding'] = enc
        current_config['Data path'] = data_path
        current_config['Export path'] = export_path
        current_config['Error path'] = error_path
        json.dump(current_config, file, indent=True)


def export_data_to_csv():
    """
    Exports data from data.dat binary file to csv file
    """
    data = load_data()
    with open(current_config['Export path'], 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def log_error(exc_type: type, exc_value, exc_tb: traceback):
    """
    Logs exception into XML file
    :param exc_type: Exception type from sys.exc_info()
    :param exc_value: Exception value from sys.exc_info()
    :param exc_tb: Traceback from sys.exc_info()
    """
    error_time = datetime.today().__str__()
    traceback_str = ''
    for trb in traceback.format_tb(exc_tb):
        traceback_str += trb
    if not os.path.exists(current_config['Error path']):
        root = ET.Element("Error_log")
        tree = ET.ElementTree(root)
    else:
        tree = ET.parse(current_config['Error path'])
    exc = ET.SubElement(tree.getroot(), "Exception")
    ET.SubElement(exc, 'Type').text = exc_type.__name__
    ET.SubElement(exc, 'Value').text = exc_value.__str__()
    ET.SubElement(exc, 'Traceback').text = traceback_str
    ET.SubElement(exc, 'Time').text = error_time
    ET.indent(tree, space="\t", level=0)
    tree.write(current_config['Error path'])
