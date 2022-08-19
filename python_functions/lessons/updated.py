# Цель данного упражнения — функция updated(). Эта функция должна принимать
# словарь в качестве единственного позиционного аргумента (обязательного) и
# произвольное кол-во именованных аргументов. Возвращать же функция должна
# новый словарь, в котором ключи, соответствующие именованным аргументам,
# должны иметь сопутствующие значения (см.примеры).

def updated(d, **kwargs):
    result = d.copy()
    result.update(kwargs)
    return result


d = {'a': 1, 'b': False}
assert updated(d, a=2, b=True, c=None) == {'a': 2, 'b': True, 'c': None}
assert d == {'a': 1, 'b': False}
assert (updated(d) == d) is True
assert (updated(d) is d) is False
