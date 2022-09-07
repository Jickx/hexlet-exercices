# Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает
# результат сравнения в виде словаря. Ключами результирующего словаря будут
# все ключи из двух входящих, а значением строка с описанием отличий: added,
# deleted, changed или unchanged.
# Возможные значения:
# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но значения
# отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми
# значениями

def gen_diff(data1: dict, data2: dict) -> dict:
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data2:
            result[key] = 'deleted'
        elif key not in data1:
            result[key] = 'added'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        elif data1[key] != data2[key]:
            result[key] = 'changed'
    return result


assert gen_diff({}, {"two": "own"}) == {"two": "added"}
assert gen_diff({"one": "eon"}, {}) == {"one": "deleted"}

assert gen_diff(
    {"three": "eerht"},
    {"four": "ruof"},
) == {
    "three": "deleted",
    "four": "added",
}

assert gen_diff(
    {"five": 5, "six": 6},
    {"six": "xis", "five": 5},
) == {
    "six": 'changed',
    "five": 'unchanged',
}

assert gen_diff(
    {"seven": "neves"},
    {"eighth": True},
) == {
    "seven": "deleted",
    "eighth": "added",
}
