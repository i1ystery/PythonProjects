import pickle
import json
import csv
from Person import Person
from datetime import date


config = {
    'Language': '',
    'Encoding': '',
    'Data path': ''
}
Languages = ['English', 'Czech']
Encodings = ['utf-8', 'ascii']
data_path = 'data.dat'
export_path = 'export.csv'
config_path = 'cfg.json'


def insert_data(pers: Person):
    with open(data_path, 'ab') as file:
        pickle.dump(pers, file)


def load_data():
    with open(data_path, 'rb') as file:
        person_list = []
        try:
            while True:
                person = pickle.load(file)
                person_list.append(person.get_as_list())
        except EOFError:
            return person_list


def create_config_file():
    with open(config_path, 'w') as file:
        config['Language'] = Languages[0]
        config['Encoding'] = Encodings[0]
        config['Data path'] = data_path
        json.dump(config, config_path, sort_keys=True, indent=True)


def export_data_to_csv():
    data = load_data()
    with open(export_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def log_error(e: Exception):
    error_time = date.today()


p = Person('Max', 'Kuzma', '2002-2-2', 'job', '123123123')
p2 = Person('Max', 'Kuzma', '2002-2-2', 'job', '123123123')
insert_data(p)
insert_data(p2)
load_data()
export_data_to_csv()