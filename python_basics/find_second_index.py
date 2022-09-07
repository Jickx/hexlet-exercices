def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN (write your solution here)
def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    second = find_index(value, iterator)
    if first is not None and second is not None:
        return first + second + 1   


print(find_second_index('b', 'bob'))  # 2
print(find_second_index('a', 'cat')) is None  # True
print(find_second_index('!', ''))
print(find_second_index('n', 'banana'))
