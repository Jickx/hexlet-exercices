# Вам предстоит реализовать функцию call_twice(), которая:
# Принимает функцию и произвольный набор аргументов для этой функции
# Дважды вызывает переданную функцию с заданными аргументами и возвращает пару
# значений – результаты двух последовательных вызовов переданной функции.
# Расположение элементов в паре соответствует порядку вызовов функции.


def call_twice(function, *args, **kwargs):
    return (function(*args, **kwargs), function(*args, **kwargs))


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


assert call_twice(push_and_count, [], value=42) == (1, 2), (
    "Function should be called twice with same arguments!"
)
assert call_twice(shoot) == ('Bang!', 'Bang!')
