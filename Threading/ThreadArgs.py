import threading


def vypisPrikladNasobeni(a,b):
    print(str(a) + " x " + str(b) + " = " +str(a*b))

if __name__ == '__main__':
    t1 = threading.Thread(target=vypisPrikladNasobeni, args=(10, 20))
    t1.start()