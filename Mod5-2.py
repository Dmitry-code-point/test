import math


class Point:

    def __init__(self, list_x, list_y):
        self.x = float(list_x)
        self.y = float(list_y)

    def select_vector(self, list_vector):
        self.vector = float(list_vector)

    def select_tilt(self, list_tilt):
        self.tilt = float(list_tilt)


    def distance(self, other_point):
        return math.sqrt(abs(self.x  - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def change_vector(self):
        return ((self.x + self.vector) * math.cos(self.tilt),
                (self.y + self.vector) * math.sin(self.tilt))

p1 = Point(5,3)
p2 = Point(2,3)
p1.select_vector(input('Введите длину переноса точки: '))
p1.select_tilt(input('Введите градус переноса точки: '))
distance_points = p1.distance(p2)
print(f"Расстояние между точками: {distance_points}")
change_point = p1.change_vector()
print(f"Новые координаты перенесенной точки: {change_point}")