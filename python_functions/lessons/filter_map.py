# Реализуйте функцию filter_map(), которая ведёт себя подобно filter() и map(),
# работающим вместе. filter_map() должна принимать в качестве аргументов
# функцию и итерируемый источник, а возвращать должна список.
# В теле filter_map() к каждому значению из источника нужно применять функцию,
# которая в ответ будет возвращать пару:

# Булево значение,
# Некий результат.
# Если булево значение (1) истинно, то результат (2) должен попадать в
# результирующий список. В противном случае второе значение пары игнорируется.


def filter_map(function, nums: list[int]) -> list[str]:
    result = []
    for i in nums:
        el = make_stars(i)
        if el[0]:
            result.append(el[1])
    return result


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)
# => *
# => *****
# => **
