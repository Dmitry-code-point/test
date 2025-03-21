import math


class Point:

    def coordinate_old_x(self, old_x):
        self.old_x = float(old_x)

    def coordinate_old_y(self, old_y):
        self.old_y = float(old_y)

    def vector(self, vector):
        self.vector = float(vector)

    def tilt(self, tilt):
        self.tilt = float(tilt)

    def get(self):
        print(f"Координаты  первой точки: {self.old_x}:{self.old_y}")

    def change_vector_x(self):
        return (self.old_x + self.vector)* math.cos(self.tilt)

    def change_vector_y(self):
        return (self.old_y + self.vector)* math.sin(self.tilt)


while True:
    a = Point()
    a.coordinate_old_x(input('Введите координату Х первой точки: '))
    a.coordinate_old_y(input('Введите координату Y первой точки: '))
    a.vector(input('Введите длину переноса точки: '))
    a.tilt(input('Введите градус переноса точки: '))
    new_x = a.change_vector_x()
    new_y = a.change_vector_y()
    print(f"Новые координаты перенесенной точки на расстояние: [{new_x}:{new_y}]")
