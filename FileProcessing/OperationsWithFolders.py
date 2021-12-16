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

path = 'D:\GitHub\FileProcessing\Max'


def show_all_folders(d):
    print('Folder: ' + d)
    directory_contents = os.listdir(d)
    for item in directory_contents:
        try_path = path + '\\' + item
        if os.path.isdir(try_path):
            show_all_folders(try_path)
        else:
            print('File: ' + item)


show_all_folders(path)
