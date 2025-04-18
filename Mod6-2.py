import time
from threading import Thread
from datetime import datetime


def get_thread(item):
    time.sleep(1)
    return print(item)


names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']
t1 = datetime.now()

for item in names:
    get_thread(item)
time_consistent = (datetime.now()- t1).total_seconds()

t2 = datetime.now()
threads = [Thread(target=get_thread, args=(item, )) for item in names]

for t in threads:
    t.start()

for t in threads:
    t.join()

time_parallel = (datetime.now()- t2).total_seconds()

print('\nЗатраченое время при последовательном:', time_consistent,
      '\nЗатраченое время при паралельном', time_parallel)
