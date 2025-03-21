import math


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def vector(self, vector):
        self.vector = float(vector)

    def tilt(self, tilt):
        self.tilt = float(tilt)


    def distance(self, other_point):
        return math.sqrt(abs(self.x  - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def change_vector_x(self):
        return (self.x + self.vector) * math.cos(self.tilt)

    def change_vector_y(self):
        return (self.y + self.vector) * math.sin(self.tilt)


p1 = Point(5,3)
p2 = Point(2,3)
p1.vector(input('Введите длину переноса точки: '))
p1.tilt(input('Введите градус переноса точки: '))
distance_points = p1.distance(p2)
print(f"Расстояние между точками: {distance_points}")
new_x = p1.change_vector_x()
new_y = p1.change_vector_y()
print(f"Новые координаты перенесенной точки: [{new_x}:{new_y}]")