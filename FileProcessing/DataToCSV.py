import csv
import os.path


def save_csv(company_name, ico, phones, description):
    header = ['Company name', 'ICO', 'Phones', 'Description']
    data = [company_name, ico, phones, description]
    if os.path.exists('businesses.csv'):
        with open('businesses.csv', 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    else:
        with open('businesses.csv', 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)


def load_csv():
    with open('businesses.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = []
        for reader_row in reader:
            if reader_row[3] != '':
                rows.append(reader_row)
        return rows


save_csv("SPSE Jecna", 61385301, ["224941469", "224942066"], """Škola nabízí obory: 
- Informatika
- Elektrotechnika
a její ředitel říka: "Je to nejlepší škola v Praze".
""")

save_csv("Seznam.cz", 26168685, "234694111", None)

save_csv("PPF A.S", 25099345, None, "Zkratka 'PPF' znamená první privatizační fond.")


for row in load_csv():
    print(row[0] + ' ' + row[1] + '\n')

