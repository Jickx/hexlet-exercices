# Реализуйте функцию chunked, которая принимает на вход число и
# последовательность. Число задает размер чанка (куска). Функция должна
# вернуть список, состоящий из чанков указанной размерности. При этом список
# должен делиться на куски-списки, строка — на строки, кортеж — на кортежи!

def chunked(chunk, items):
    output = []
    for i in range(0, len(items), chunk):
        output.append(items[i:i + chunk])
    return output


assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
assert chunked(3, ['a', 'b', 'c', 'd']) == [['a', 'b', 'c'], ['d']]
assert chunked(3, 'foobar') == ['foo', 'bar']
assert chunked(10, (42,)) == [(42,)]
