import json


class Model:
    def save_to_file(self, words):
        attributes = dir(words)
        word_keys = list(words.keys())
        combined_attribute = attributes + word_keys
        with open('words.json', 'w') as file:
            json.dump(combined_attribute, file, ensure_ascii=False)

    def open_file(self,):
        with open('words.json', 'r') as file:
            data_words = json.load(file)
            data_words1 = list(filter(lambda item: not item.startswith('_'), data_words)) # Избавление  от служеюных аттрибут
            data_words2 = []
            for item in data_words1:
                if item in words:
                    data_words2.append(item)
            print(data_words) # Вывод задания IN 2 - OUT 2
            print (data_words2)


model = Model()

words = {'title': 1, 'text': 2, 'author': 3}

model.save_to_file(words)
model.open_file()

