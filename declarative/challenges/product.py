# Вам предстоит реализовать функцию product(), которая принимает один и более
# позиционных параметров — iterable любого вида, и возвращает список кортежей.
# Возвращаемый список представляет собой декартово произведение элементов
# входных последовательностей — все сочетания "каждый с каждым". Например, для
# последовательностей [1, 2] и 'ab' (помним, строки — тоже iterable) функция
# должна вернуть список [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')], то есть
# каждый элемент списка с каждым символом строки.

import itertools


def product(seq, *args):
    somelist = [seq]
    for i in args:
        somelist.append([char for char in i])
    return list(itertools.product(*somelist))


# product()  # хотя бы одна последовательность должна быть дана
# Traceback (most recent call last):
#    ...
# TypeError: product() missing 1 required positional argument: 'sequence'
assert list(product([])) == []
assert list(product([1, 2], 'abc')) == [
    (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
assert list(product('hello', [], 'world')) == []
# ^ если хотя бы одна из входных последовательностей пустая,
# то выходной список тоже будет пуст
assert isinstance(product([]), list) is True
