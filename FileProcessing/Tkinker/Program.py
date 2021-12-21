import os
import pickle
import json
import csv
import traceback
import xml.etree.cElementTree as ET
from datetime import datetime


default_config = {
    'Language': 'English',
    'Encoding': 'utf-8',
    'Data path': './data.dat',
    'Export path': './export.csv',
    'Error path': './error.log'
}
config_path = 'cfg.json'
current_config = {}
data_to_save = []


def create_person(name, lastname, job, phone_number):
    data_to_save.append([name, lastname, job, phone_number])


def export_persons():
    with open(current_config['Data path'], 'ab') as file:
        for obj in data_to_save:
            pickle.dump(obj, file)


def load_data():
    with open(current_config['Data path'], 'rb') as file:
        person_list = []
        try:
            while True:
                person = pickle.load(file)
                person_list.append(person)
        except EOFError:
            return person_list


def create_config():
    with open(config_path, 'w') as file:
        json.dump(default_config, file, indent=True)


def load_config():
    global current_config
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            current_config = json.load(file)
    else:
        create_config()
        current_config = default_config


def save_changes_to_config(lang, enc, data_path, export_path, error_path):
    with open(config_path, 'w') as file:
        current_config['Language'] = lang
        current_config['Encoding'] = enc
        current_config['Data path'] = data_path
        current_config['Export path'] = export_path
        current_config['Error path'] = error_path
        json.dump(current_config, file, indent=True)


def export_data_to_csv():
    data = load_data()
    with open(current_config['Export path'], 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def log_error(exc_type, exc_value, exc_tb):
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

