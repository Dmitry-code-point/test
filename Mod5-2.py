import math


class Point:

    old_x = 0
    old_y = 0

    def coordinate_old_x(self, old_x):
        self.old_x = float(old_x)

    def coordinate_old_y(self, old_y):
        self.old_y = float(old_y)

    def coordinate_new_x(self, new_x):
        self.new_x = float(new_x)

    def coordinate_new_y(self, new_y):
        self.new_y = float(new_y)

    def distance(self):
        return math.sqrt(abs((self.new_x - self.old_x) * 2 + (self.new_y - self.old_y) * 2))

    def get(self):
        print(f"Координаты  первой точки: {self.old_x}:{self.old_y}\n"
             f"Координаты второй точки: {self.new_x}:{self.new_y}")

while True:
    a = Point()
    a.coordinate_old_x(input('Введите координату Х первой точки: '))
    a.coordinate_old_y(input('Введите координату Y первой точки: '))
    a.coordinate_new_x(input('Введите координату Х второй точки: '))
    a.coordinate_new_y(input('Введите координату Y второй точки: '))
    a.get()
    print(f"Расстояние между точками: {a.distance()}")


