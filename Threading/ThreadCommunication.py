import csv
import threading
import time

data = []
with open('dluznici.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # skip the headers
    for row in reader:
        data.append(row);

start = time.time()
# OPTIMALUZUJTE ZDE - ZACATEK
stop_threads = False
result = None


def hledej(od, do, rodnecislo):
    global stop_threads
    global result
    for i in range(od, do):
        if not stop_threads:
            if data[i][1] == rodnecislo:
                stop_threads = True
                result = i
                return
        else:
            return


data_split = len(data)//4
rod_cis = '916107/5649'
v1 = threading.Thread(target=hledej(0, data_split, rod_cis))
v2 = threading.Thread(target=hledej(data_split, data_split*2, rod_cis))
v3 = threading.Thread(target=hledej(data_split*2, data_split*3, rod_cis))
v4 = threading.Thread(target=hledej(data_split*3, data_split*4, rod_cis))
v1.start()
v2.start()
v3.start()
v4.start()


print(result)

# OPTIMALUZUJTE ZDE - KONEC
end = time.time()
print("Vypocet trval {:.6f} sec.".format((end - start)))