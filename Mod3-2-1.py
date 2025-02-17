l = [1, 4, 1, 6, 5, 7, 'hello', 'a', 5, 'hello']
d = []
for i in l:
	if i not in d:
		d.append(i)
print('Вводные данные:',l)
print('Повторяющиеся элементы в единственном экземпляре:',d)
