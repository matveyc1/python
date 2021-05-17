def fun(name, surname, year, city, email, telephone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {user.get("city")}, '
          f'email: {email}, Телефон: {telephone}')
    return


user = {'name': 'Иван', 'surname': 'Иванов', 'year': '1998', 'city': 'Москва', 'email': 'test@bk.ru',
        'telephone': '100000'}
print(fun(user.get('name'), user.get('surname'), user.get('year'), user.get('city'), user.get('email'),
          user.get('telephone')))
