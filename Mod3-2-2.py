from random import randint
n = 5
m = [[randint(0,100)
	for i in range(n)]
		for j in range(n)
	]
find_element = max(max(sublist)
	for sublist in m)
print('Ввод данных:',m)
print('Вывод:',find_element)