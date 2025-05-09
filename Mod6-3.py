import time
from threading import Thread
from datetime import datetime

import requests


def get_html(item):
    response = requests.get(item)
    return print(response.text)

html_name = ['https://yandex.ru',
             'https://google.com',
             'https://ru.wikipedia.org',
             'https://dzen.ru/?yredirect=true',
             'https://mail.ru/']
t1 = datetime.now()

for name in html_name:
    get_html(name)
time_consistent = (datetime.now()- t1).total_seconds()

t2 = datetime.now()
threads = [Thread(target=get_html, args=(item, )) for item in html_name]

for t in threads:
    t.start()

for t in threads:
    t.join()

time_parallel = (datetime.now()- t2).total_seconds()

print('\nЗатраченое время при последовательном:', time_consistent,
      '\nЗатраченое время при паралельном', time_parallel)
