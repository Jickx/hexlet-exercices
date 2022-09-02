# Реализуйте функцию find_index_of_nearest(), которая принимает на вход список
# чисел и искомое число. Задача функции — найти в списке ближайшее число к
# искомому и вернуть его индекс.
# Если в списке содержится несколько чисел, одновременно являющихся ближайшими
# к искомому числу, то возвращается наименьший из индексов ближайших чисел.


def find_index_of_nearest(number: int, numbers: list[int]) -> int:
    if not numbers:
        return None
    diff = min(numbers, key=lambda x: abs(number - x))
    return numbers.index(diff)


assert find_index_of_nearest(2, []) is None
assert find_index_of_nearest(0, [10]) == 0
assert find_index_of_nearest(0, [10, 15]) == 0
assert find_index_of_nearest(1, [15, 10]) == 1
assert find_index_of_nearest(12, [15, 10]) == 1
assert find_index_of_nearest(0, [15, 10, 3, 4]) == 2
assert find_index_of_nearest(4, [7, 5, 3, 2]) == 1
assert find_index_of_nearest(4, [7, 5, 4, 4, 3, 6]) == 2
