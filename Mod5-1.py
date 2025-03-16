class StringVar:

    def word(self):
        self.word = ""
    def set(self, list_words):
        self.word = list_words
    def get(self):
        return self.word

while True:
    a = StringVar()
    a.set(input('Введите словосочетание: '))
    print(a.get())



