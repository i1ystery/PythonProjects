import os
from concurrent.futures import ProcessPoolExecutor
from tkinter.filedialog import askdirectory
from itertools import repeat
import shutil


def find_request(log_folders, path, vld_path, request):
    for log in log_folders:
        log_path = os.path.join(path, log)
        with open(os.path.join(log_path, 'Passwords.txt')) as f:
            txt = f.read()
            if request in txt:
                print(txt)
                print(log_path)
                print(vld_path)
                shutil.move(log_path, vld_path)


def ask_log_data():
    request = input('Enter request: ')
    path = askdirectory(initialdir=os.getcwd(), title='Choose folder with logs')
    logs = os.listdir(path)
    vld_path = askdirectory(initialdir=os.getcwd(), title='Choose folder for valid logs')
    return logs, path, vld_path, request


def run():
    logs, path, vld_path, request = ask_log_data()
    # Split list
    if len(logs) >= 4:
        max_workers = 4
    else:
        max_workers = 1
    chunk_size = len(logs)//max_workers
    chunk_list = list()
    for i in range(0, len(logs), chunk_size):
        chunk_list.append(logs[i:i+chunk_size])
    # Run multiprocess
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(find_request, chunk_list, repeat(path), repeat(vld_path), repeat(request))


if __name__ == '__main__':
    run()