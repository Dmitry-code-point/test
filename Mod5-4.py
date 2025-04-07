import json


def save_to_file(words):
    attributes = dir(words) + list(words.keys())
    with open('words.json', 'w') as file:
        json.dump(attributes, file, ensure_ascii=False)

def open_file():
    with open('words.json', 'r') as file:
        data_attributes = json.load(file)
        print(data_attributes) # Вывод задания IN 2 - OUT 2
        return get_attribute(data_attributes)

def get_attribute(data_words):
    data_words1 = list(filter(lambda item: not item.startswith('_'), data_words)) # Избавление  от служеюных аттрибут
    data_words2 = []
    for item in data_words1:
        if item in words:
            data_words2.append(item)
    print(data_words2)


words = {'title': 1, 'text': 2, 'author': 3}
save_to_file(words)
words = open_file()

