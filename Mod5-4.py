import json


class Model:
    def Save_to_file(self, words):
        with open('words.json', 'w') as file:
            json.dump(words, file, ensure_ascii=False)

    def Open_file(self,):
        with open('words.json', 'r') as file:
            data_words = json.load(file)
            print(data_words)


model = Model()

words = {"title": "1", "text": 2, "author": "3"}

model.Save_to_file(words)
model.Open_file()