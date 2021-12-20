import json
import os


def save_json(company_name, ico, phones, description):
    input_data = {
        'Company name': company_name,
        'ICO': ico,
        'Phones': phones,
        'Description': description
    }
    if os.path.exists('businesses.json'):
        with open('businesses.json', 'r', encoding='utf-8') as f:
            data_to_write = json.load(f)
            data_to_write['Businesses'].append(input_data)
        with open('businesses.json', 'w', encoding='utf-8') as f:
            json.dump(data_to_write, f, ensure_ascii=False, indent=True)
    else:
        data_to_write = {'Businesses': [input_data]}
        with open('businesses.json', 'w', encoding='utf-8') as f:
            json.dump(data_to_write, f, ensure_ascii=False, indent=True)


def load_json():
    with open('businesses.json', encoding='utf-8') as f:
        data_to_write = json.load(f)
        objects = data_to_write['Businesses']
        rows = []
        for reader_row in objects:
            if reader_row['Description'] is not None:
                rows.append(reader_row)
        return rows


save_json("SPSE Jecna", 61385301, ["224941469", "224942066"], """Škola nabízí obory:
- Informatika
- Elektrotechnika
a její ředitel říka: "Je to nejlepší škola v Praze".
""")

save_json("Seznam.cz", 26168685, "234694111", None)

save_json("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")


a = load_json()
for businesses in a:
    print(businesses['Company name'] + ' ' + str(businesses['ICO']))
