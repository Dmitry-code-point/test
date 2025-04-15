import time
from threading import Thread


def get_thread(item):
    time.sleep(1)
    return print(item)


names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']

for item in names:
    get_thread(item)
