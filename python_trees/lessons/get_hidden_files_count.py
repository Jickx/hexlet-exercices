items = [2, [3, [4, [5, [6]]], [7]]]


def check(num):
    if num % 2 == 0 and num > 4:
        return num
    return 1


def agregate(items):
    if isinstance(items, int):
        return check(items)
    result = list(map(agregate, items))
    return sum(result)


print(agregate(items))
