# Цель упражнения — функция collect_indexes(). Эта функция должна принимать на
# вход коллекцию (некий iterator/iterable) и возвращать словарь (или подобная
# ему коллекция!), где ключом будет элемент коллекции, а значением для ключа —
# список индексов коллекции, по которым встречается этот элемент.


def collect_indexes(items):
    output = {}
    for i in range(len(items)):
        output.setdefault(items[i], []).append(i)
    return output


assert not collect_indexes([])
assert collect_indexes([1]) == {1: [0]}
assert collect_indexes([1, 2]) == {1: [0], 2: [1]}
assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}
