import json
def register():
    data={}
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
        elif action == 'Вход':
            login = input('Введите логин: ').strip()
            if login in data.keys():
                passwd = input('Введите пароль:')
                if passwd in data.keys():
                    print('Вход выполнен.')
                else:
                    print('Неверный пароль.')
            else:
                print('Неверный логин')
        with open('data.json', 'a',
                  encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            print('Данные записаны')
register()