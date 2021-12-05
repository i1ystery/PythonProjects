data = []
with open('imports-85.txt', 'r') as myfile:
    data = myfile.readlines()
parsed_list = []
for i in data:
    print('Not parsed')
    row_parsed = ''
    row = i.strip().split(',')
    print(row)
    if row[1] == '?':
        row[1] = '65'
    if row[5] == '?':
        row[5] = 'two'
    if row[18] == '?':
        row[18] = '2.54'
    if row[19] == '?':
        row[19] = '2.07'
    if row[21] == '?':
        row[21] = '48'
    if row[22] == '?':
        row[22] = '4150'
    if row[25] == '?':
        row[25] = '5118'
    print(row)
    print('Parsed')
    for j in row:
        j = j.strip()
        try:
            a = int(j)
            row_parsed += j + ','
        except Exception:
            try:
                a = float(j)
                row_parsed += j + ','
            except Exception:
                row_parsed += "\'" + j + "\'" + ","
    parsed_list.append(row_parsed)

textfile = open("parsed_inserts.txt", "w")
for element in parsed_list:
    lenght = len(element)
    textfile.write("(" + element[0:lenght - 1] + "),\n")
textfile.close()
