import pickle
import datetime


try:
    with open('info.dat', 'rb') as file:
        info = pickle.load(file)
        print(info)
        info['pocet_spusteni'] += 1
        info['posledni_spusteni'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open('info.dat', 'wb') as f:
            pickle.dump(info, f)
except Exception:
    print('Soubor info.dat neexistuje, proto bude vytvoren novy.')
    with open('info.dat', 'wb') as file:
        info = {'pocet_spusteni': 0, 'posledni_spusteni': None}
        pickle.dump(info, file)

