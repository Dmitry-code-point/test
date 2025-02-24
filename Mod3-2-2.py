from random import randint
n = 5
#m = [[randint(0,100)
#	for i in range(n)]
#		for j in range(n)
#	]
m = [[9, 70, 20, 67, 33], 
	 [60, 20, 94, 14, 77], 
	 [27, 58, 45, 0, 13],
	 [39, 47, 25, 97, 69],
	 [83, 13, 100, 1, 85]
	 ]
find_element = max(max(sublist)
	for sublist in m
	)
print('Ввод данных:',m)
print('Вывод:',find_element)