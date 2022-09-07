# Реализуйте функцию merged(), которая объединяет несколько словарей в один
# общий словарь. Функция принимает список словарей и возвращает результат в
# виде словаря, в котором каждый ключ содержит множество (set) уникальных
# значений.

def merged(items: list[dict]) -> dict:
    output = {}
    for item in items:
        for k, v in item.items():
            output.setdefault(k, set()).add(v)
    return output


assert (merged([{}, {}]) == {}) is True
assert (merged([
    {'a': 1, 'b': 2},
    {'b': 10, 'c': 100},
]) == {'a': {1}, 'b': {2, 10}, 'c': {100}}) is True
