# Реализуйте функцию convert(), которая принимает на вход список определённой
# структуры и возвращает словарь, полученный из этого списка.

# Список устроен таким образом, что с помощью него можно представлять словари.
# Каждый элемент списка — тоже список из двух элементов, где первый элемент —
# ключ, а второй — значение. Значение тоже может быть списком. Любой список
# внутри исходного списка всегда рассматривается как данные, которые нужно
# конвертировать в словарь.


def convert(tree):

    def walk(subtree):
        key, value = subtree
        return key, convert(value) if isinstance(value, list) else value

    return dict(map(walk, tree))

tree = [
    ['key4', 'value4'],
    ['anotherKey', [
        ['key7', False],
        ['innerKey', []],
    ],
     ],
    ['key6', None],
    ['anotherKey2', [
        ['wow', [['one', 'two'], ['three', 'four']]],
        ['key5', True],
    ],
     ],
]

expected = {
    'key4': 'value4',
    'anotherKey': {'key7': False, 'innerKey': {}},
    'key6': None,
    'anotherKey2': {'wow': {'one': 'two', 'three': 'four'}, 'key5': True},
}


assert convert(tree) == expected
