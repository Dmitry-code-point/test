import json

class Model:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def get_attribute(self):
        all_attributes = dir(self)
        #print(all_attributes) # Вывод задания IN 2 - OUT 2
        need_attributes = list(filter(lambda item: not item.startswith('_'), all_attributes))  # Избавление  от служеюных аттрибут
        name_functions = ['save_to_file', 'open_file', 'get_attribute']
        attributes = []
        for item in need_attributes:
            if item not in name_functions:
                attributes.append(item)
        return self.save_to_file(attributes)

    def save_to_file(self,old_attributes):
        new_attributes = old_attributes
        with open('words.json', 'w') as file:
            json.dump(new_attributes, file, ensure_ascii=False)

    def open_file(self):
        with open('words.json', 'r') as file:
            return json.load(file)
        
m = Model(1, 2, 3)
m.get_attribute()
load_data = m.open_file()
print(load_data)
