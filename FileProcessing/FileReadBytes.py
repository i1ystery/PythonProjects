import time

try:
    with open('lock.dat', 'wb') as f:
        print(f.read(1))
        if f.read(1) == bytes(0x00):
            f.write(bytes(0xFF))
            f.flush()
            time.sleep(10)
            with open('lock.dat', 'wb') as file:
                file.write(bytes(0x00))
        else:
            print('Another instance is running.')
        # Do something with the file
except FileNotFoundError:
    with open('lock.dat', 'wb') as f:
        f.write(bytes(0x00))