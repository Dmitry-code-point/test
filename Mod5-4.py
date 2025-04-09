import json

class Model:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def save_to_file(self):
        all_attributes = dir(self)
        with open('words.json', 'w') as file:
            json.dump(all_attributes, file, ensure_ascii=False)

    def open_file(self):
        with open('words.json', 'r') as file:
            data_attributes = json.load(file)
            print(data_attributes)  # Вывод задания IN 2 - OUT 2
            return self.get_attribute(data_attributes)

    def get_attribute(self, data_words):
        data_words1 = list(
            filter(lambda item: not item.startswith('_'), data_words))  # Избавление  от служеюных аттрибут
        name_functions = ['save_to_file', 'open_file', 'get_attribute']
        attributes = []
        for item in data_words1:
            if item not in name_functions:
                attributes.append(item)
        print(attributes)

m = Model(1, 2, 3)
m.save_to_file()
m.open_file()

