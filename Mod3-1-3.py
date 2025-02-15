a = int(input('Введите число: '))
s = 0
def number(a, s):
	while (a > 0):
		s = s + ( a % 10)
		a = a // 10
	return s
print(number(a, s))