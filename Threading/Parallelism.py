import csv
import multiprocessing as mp
import time

data = []
with open('dluznici.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)  # skip the headers
    for row in reader:
        data.append(row)


def rok_narozeni_z_rc(rodne_cislo):
    assert type(rodne_cislo) == str
    assert len(rodne_cislo) == 11

    rok_narozeni = int(rodne_cislo[0:2])
    if (rok_narozeni > 21):
        rok_narozeni += 1900
    else:
        rok_narozeni += 2000
    return rok_narozeni


def prumerny_dluh_dle_roku_narozeni(rokOd, rokDo, label):
    soucet = 0
    pocet = 0
    prumerny_dluh = 0
    for i in range(0, len(data)):
        if (rokOd <= rok_narozeni_z_rc(data[i][1]) < rokDo):
            pocet += 1
            soucet += int(data[i][2])
    if (pocet > 0):
        prumerny_dluh = round(soucet / pocet)
    print("Prumerny dluh pro " + label + " je " + str(prumerny_dluh) + " CZK")


if __name__ == "__main__":
    start = time.time()
    # OPTIMALUZUJTE ZDE - ZACATEK

    v1 = mp.Process(target=prumerny_dluh_dle_roku_narozeni, args=(1991, 2001, "dvacatniky"))
    v2 = mp.Process(target=prumerny_dluh_dle_roku_narozeni, args=(1981, 1991, "tricatniky"))
    v3 = mp.Process(target=prumerny_dluh_dle_roku_narozeni, args=(1971, 1981, "ctyricatniky"))
    v4 = mp.Process(target=prumerny_dluh_dle_roku_narozeni, args=(1961, 1971, "padesatniky"))
    v5 = mp.Process(target=prumerny_dluh_dle_roku_narozeni, args=(1951, 1961, "sedesatniky"))
    v1.start()
    v2.start()
    v3.start()
    v4.start()
    v5.start()

    # OPTIMALUZUJTE ZDE - KONEC
    end = time.time()
    print("Vypocet trval {:.6f} sec.".format((end - start)))