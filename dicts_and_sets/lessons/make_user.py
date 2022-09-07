# В этой практике вам нужно реализовать две функции:
# функцию make_user(), которая должна принимать два параметра — имя
# пользователя и возраст (число). Вернуть функция должна словарь с ключами
# 'name' и 'age', по которым должны быть сохранены соответствующие значения.
# функцию format_user(), которая, будучи применена к результату вызова
# make_user() (помним — это словарь), должна вернуть строку вида 'Phil, 25'.

def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(person):
    return f"{person['name']}, {person['age']}"


bob = make_user('Bob', 42)
assert len(bob) == 2
assert 'name' in bob
assert 'age' in bob
assert bob['name'] == 'Bob'
assert bob['age'] == 42

assert format_user(make_user('Joe', 30)) == 'Joe, 30'
assert format_user(make_user('Ann', 20)) == 'Ann, 20'
