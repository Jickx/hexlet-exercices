# Привычные нам структуры можно представить и как рекурсивные. Например, у
# списка, есть голова (первый элемент) и хвост (последущие), у хвоста тоже
# есть своя голова и хвост, который тоже можно разделить на голову и хвост. И
# так далее до конца, где последний элемент списка можно представить как
# голова плюс хвост из пустого списка. А вот уже пустой список невозможно
# разделить, и наша рекурсия остановится.


# length() принимает список и возвращает его длину

def length(nums):
    if nums == []:
        return 0
    return 1 + length(nums[1:])


assert length([1, 2, 3]) == 3

# reverse_range() принимает два числа begin и end и возвращает перевернутый
# список всех чисел между. Для простоты договоримся, что begin <= end


def reverse_range(begin, end):
    if end == begin:
        return [end]
    return [end] + reverse_range(begin, end - 1)


assert reverse_range(1, 1) == [1]
assert reverse_range(1, 3) == [3, 2, 1]


# filter_positive() принимает список чисел и возвращает новый только с
# положительными элементами

def filter_positive(numbers):
    if not numbers:
        return []
    head, *tail = numbers
    if head > 0:
        return [head] + filter_positive(tail)
    return filter_positive(tail)


print(filter_positive([]))  # []
print(filter_positive([-3]))  # []
print(filter_positive([1, -2, 3]))  # [1, 3]
