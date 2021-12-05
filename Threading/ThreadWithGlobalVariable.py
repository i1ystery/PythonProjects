import threading

nakupniSeznam = ["Mleko", "Maslo", "Rohlik"]


def vypisNakupniSeznam():
    global nakupniSeznam
    for i in nakupniSeznam:
        print(i)



vlakno = threading.Thread(target=vypisNakupniSeznam)
vlakno.start()
vlakno.join()