d = {
	'name1': 'id1', 'name2': 'id2', 'name3': 'id3'
	}
smena = {
	value: key for key, value in d.items()
	}
print("Вводные данные:", d)
print("Вывод:", smena)