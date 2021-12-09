import threading
from concurrent.futures import ThreadPoolExecutor


class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
    def vloz_mince(self, pocetKusu, mince):
        for i in range(0, pocetKusu):
            self.zustatek += mince
    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)


mujUcet = BankovniUcet(0)
vklad = [(1000, 1), (1000, 2), (1000, 5), (1000, 10)]

with ThreadPoolExecutor(max_workers=len(vklad)) as executor:
    executor.map(lambda f: mujUcet.vloz_mince(*f), vklad)

print(mujUcet)