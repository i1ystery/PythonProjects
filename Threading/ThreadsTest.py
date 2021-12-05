import threading
import time


def print_num():
    a_range = range(0, 11)
    a_range = reversed(a_range)
    for i in a_range:
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    print("ZACATEK PROGRAMU")
    t1 = threading.Thread(target=print_num)
    t1.start()
    t1.join()
    print("KONEC PROGRAMU")