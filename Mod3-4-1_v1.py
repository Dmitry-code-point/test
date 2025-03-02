import json
def register():
    data={}
    while True:
        action = input('Регистрация пользователя или Вход: ')
        if action == 'Регистрация'
            login = input('Введите логин: ').strip()
            if login in data.keys():
                print('Логин занят')
                continue
            passwd = input('Введите пароль:')
            print('Регистрация завершина')
            data[login] = passwd
        with open('data.json', 'w',
                  encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
            print('Данные записаны')
register()