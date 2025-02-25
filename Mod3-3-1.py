import math
def area(a, b, c):
	pass
a = int(input('Первое число:'))
b = int(input('Второе число:'))
c = int(input('Третье число:'))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Площадь треугольника:", s)
