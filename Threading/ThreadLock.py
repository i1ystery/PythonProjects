import threading


class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
        self.lock = threading.Lock()
    def vloz_mince(self,pocetKusu, mince):
        with self.lock:
            for i in range(0, pocetKusu):
                self.zustatek += mince
    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)


mujUcet = BankovniUcet(0)

t1 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,1))
t2 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,2))
t3 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,5))
t4 = threading.Thread(target=mujUcet.vloz_mince, args=(1000000,10))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(mujUcet)