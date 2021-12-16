import os
from os import path, mkdir, rmdir, listdir
from shutil import rmtree
#
#
# print(path.isdir('Max'))
#
# mkdir('Max')
#
# print(path.isdir('Max'))
#
# rmdir('Max')
#
# print(path.isdir('Max'))
#
# mkdir('Max')
# with open('Max/hello.dat', 'w') as f:
#     f.write('Ahoj')
# mkdir('Max/Kuzma')
# print(listdir('Max'))
#
# rmtree('Max')
#
# print(path.isdir('Max'))


# mkdir('Max')
# with open('Max/hello.dat', 'w') as f:
#     f.write('Ahoj')
# mkdir('Max/Kuzma')
# with open('Max/Kuzma/sheesh.dat', 'w') as f:
#     f.write('Sheesh')


path = 'Max'

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

print(listdir_fullpath(path))
