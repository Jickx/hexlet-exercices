# Реализуйте функцию same_parity_filter(), которая принимает на вход список и
# возвращает новый список, состоящий из элементов, у которых такая же
# чётность, как и у первого элемента исходного списка.

def check_parity(num):
    return num % 2 == 0


def same_parity_filter(nums: list[int]) -> list:
    if not nums:
        return []

    parity_first_number = nums[0] % 2 == 0

    return list(filter(
        lambda x: parity_first_number == check_parity(x), nums
    ))


assert same_parity_filter([]) == []
assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
