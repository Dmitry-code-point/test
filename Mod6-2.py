import time
from threading import Thread
from datetime import datetime


def get_thread(item):
    time.sleep(1)
    return print(item)


names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']
t1 = datetime.now()

# for item in names:
#     get_thread(item)

threads = [Thread(target=get_thread, args=(item, )) for item in names]

for t in threads:
    t.start()

for t in threads:
    t.join()

print('Затраченное время:', (datetime.now()- t1).microseconds)
