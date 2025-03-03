import json
def register():
    data = {}
    while True:
        action = input('Регистрация пользователя или Вход: ')
        if action == 'Регистрация':
            login = input('Введите логин: ').strip()
            if login in data.keys():
                print('Логин занят')
            else:
                passwd = input('Введите пароль:')
                print('Регистрация завершина')
                data[login] = passwd
                with open('data.json', 'w') as file:
                    json.dump(data, file, ensure_ascii=False)
                print('Данные записаны')
        elif action == 'Вход':
            login = input('Введите логин: ').strip()
            if login in data.keys():
                passwd = input('Введите пароль:')
                if passwd in data.keys():
                    print('Вход выполнен.')
                else:
                    print('Неверный пароль.')
            else:
                print('Такого пользователя не существует.')
        else:
            print('Регистрация пользователя или Вход: ')
register()