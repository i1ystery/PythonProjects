import threading
import time


class Odpocitavani(threading.Thread):
    def setOdKolika(self, num):
        for i in range(num):
            print(num)
            num -= 1
            time.sleep(1)


if __name__ == '__main__':
    vlakno = Odpocitavani()
    vlakno.setOdKolika(10)
    vlakno.start()
    vlakno.join()