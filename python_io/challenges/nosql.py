# В этом испытании вам предстоит реализовать простой интерфейс NoSQL базы
# данных, основанной на текстовом файле. Функция get_() принимает на вход путь
# к файлу и ключ (любая строка) и возвращает значение по этому ключу. Если
# значение отсутствует, то возвращается None. Фунция set_() принимает такж
# путь к файлу, ключ и значение (любая строка), и записывает по ключу значение
# в базу.

KEY_LEN = 10
VALUE_LEN = 20


def set_(path, key, value):
    with open(path, 'r+') as db_:
        lines = db_.readline()
        for line in lines:
            if line.split(',')[0] == key:
                db_.writelines(f'{key}, {value}\n')
        if len(key) < KEY_LEN and len(value) < VALUE_LEN:
            db_.writelines(f'{key}, {value}\n')


def get_(path, key):
    with open(path) as db_:
        lines = db_.readlines()
        for line in lines:
            if line.split(',')[0] == key:
                return line.split(',')[1].strip()


db = open('./nosql.db', 'w')
path = db.name  # ./nosql.db
set_(path, 'key1', 'value1')
print(get_(path, 'key1'))  # 'value1'
set_(path, 'key2', 'value2')
print(get_(path, 'key2'))  # 'value2'
