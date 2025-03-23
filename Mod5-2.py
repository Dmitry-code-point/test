import math


select_vector = float(input("Введите число: "))
select_tilt = float(input("Введите градус угла: "))

class Point:

    def __init__(self, list_x, list_y):
        self.x = float(list_x)
        self.y = float(list_y)

    def distance(self, other_point):
        return math.sqrt(abs(self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

def change_vector(point_p):
    return ((point_p.x + select_vector) * math.cos(select_tilt),
            (point_p.y + select_vector) * math.sin(select_tilt))

p1 = Point(5,3)
p2 = Point(2,3)
distance_points = p1.distance(p2)
change_point = change_vector(p1)
print(f"Расстояние между точками: {distance_points}")
print(f"Новые координаты перенесенной точки: {change_point}")