import os
from os import path, mkdir, rmdir, listdir
from shutil import rmtree


rmtree('Max')

print(path.isdir('Max'))

mkdir('Max')

print(path.isdir('Max'))

rmdir('Max')

print(path.isdir('Max'))

mkdir('Max')
with open('Max/hello.dat', 'w') as f:
    f.write('Ahoj')
mkdir('Max/Kuzma')
print(listdir('Max'))

rmtree('Max')

print(path.isdir('Max'))


mkdir('Max')
with open('Max/hello.dat', 'w') as f:
    f.write('Ahoj')
mkdir('Max/Kuzma')
with open('Max/Kuzma/sheesh.dat', 'w') as f:
    f.write('Sheesh')


def show_all_folders(d):
    for item in os.listdir(d):
        print(os.path.join(d, item))
        if os.path.isdir(os.path.join(d, item)):
            show_all_folders(os.path.join(d, item))


directory = 'D:\GitHub'
show_all_folders(directory)
