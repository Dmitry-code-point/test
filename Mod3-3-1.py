import math
def area(a, b, c):
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	return area
a = int(input('Первое число:'))
b = int(input('Второе число:'))
c = int(input('Третье число:'))
print("Площадь треугольника:", area)
