# Реализуйте функцию same_parity_filter(), которая принимает на вход список и
# возвращает новый список, состоящий из элементов, у которых такая же
# чётность, как и у первого элемента исходного списка.


def same_parity_filter(nums: list[int]) -> list:
    if nums:
        if nums[0] % 2 == 0:
            return list(filter(lambda x: x % 2 == 0, nums))
        else:
            return list(filter(lambda x: x % 2 != 0, nums))
    else:
        return []


print(same_parity_filter([]))
# []
print(same_parity_filter([2, 0, 1, -3, 10, -2]))
# [2, 0, 10, -2]
print(same_parity_filter([-1, 0, 1, -3, 10, -2]))
# [-1, 1, -3]
