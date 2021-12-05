import threading
import time


class Print_Num(threading.Thread):
    def run(self):
        a_range = range(0, 11)
        a_range = reversed(a_range)
        for i in a_range:
            print(i)
            time.sleep(1)



if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    print_num = Print_Num()
    print_num.start()
    print_num.join()
    print("KONEC PROGRAMU")