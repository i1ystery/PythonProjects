import time

try:
    with open('lock.dat', 'rb') as f:
        if f.read(1) == bytes(0x00):
            with open('lock.dat', 'wb') as file:
                file.write(bytes(0xFF))
                file.flush()
            time.sleep(10)
            with open('lock.dat', 'wb') as file:
                file.write(bytes(0x00))
                file.flush()
        else:
            print('Another instance is running.')
except FileNotFoundError:
    with open('lock.dat', 'wb') as f:
        f.write(bytes(0x00))