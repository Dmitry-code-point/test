class StringVar:

    def word(self):
        self.words = ""
    def set(self, list_words):
        self.words = list_words
    def get(self):
        return self.words

while True:
    a = StringVar()
    a.set(input('Введите словосочетание: '))
    print(a.get())



