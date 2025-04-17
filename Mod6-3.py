import time
from threading import Thread
from datetime import datetime

import requests


def get_html(item):
    response = requests.get(item)
    #print(response.text)
    print(response.status_code)

html_name = ['https://yandex.ru', 'https://google.com', 'https://ru.wikipedia.org', 'https://dzen.ru/?yredirect=true']

for name in html_name:
    get_html(name)
