# Реализуйте функцию summary_ranges(), которая находит в списке непрерывные
# возрастающие последовательности чисел и возвращает список с их перечислением.


def summary_ranges(nums: list[int]) -> list:
    output = []
    aux = ''
    i = 0
    while i < len(nums) - 1:
        curr = nums[i]
        next = nums[i + 1]
        if not aux and next == curr + 1:
            aux = f'{curr}->'
        if aux and next != curr + 1:
            aux += f'{curr}'
            output.append(aux)
            aux = ''
        if aux and i == len(nums) - 2 and next == curr + 1:
            aux += f'{next}'
            output.append(aux)
            aux = ''
        i += 1
    return output


assert summary_ranges([]) == []
assert summary_ranges([1]) == []
assert summary_ranges([1, 2, 3]) == ['1->3']
assert summary_ranges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5']
assert summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])\
    == ['110->112', '-5->-4']
