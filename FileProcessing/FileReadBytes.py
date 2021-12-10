import time

try:
    with open('lock.dat', 'ab') as f:
        if f.read(1) == b'0x00':
            f.write(b'0xFF')
            time.sleep(10)
            f.write(b'0x00')
        else:
            print('Another instance is running.')
        # Do something with the file
except IOError:
    with open('lock.dat', 'wb') as f:
        f.write(b'0x00')