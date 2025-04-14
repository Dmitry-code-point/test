import time
from threading import Thread


def get_thread(thread_name):
    time.sleep(1)
    return thread_name

names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']

for item in names:
    thread_names = get_thread(item)
    print(thread_names)

