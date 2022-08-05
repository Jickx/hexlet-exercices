# Реализуйте функцию is_continuous_sequence(), которая проверяет, является ли
# переданная последовательность целых чисел возрастающей непрерывно (не
# имеющей пропусков чисел). Например, последовательность [4, 5, 6, 7] —
# непрерывная, а [0, 1, 3] — нет. Последовательность может начинаться с любого
# числа. Главное условие — отсутствие пропусков чисел. Последовательность из
# одного числа не может считаться возрастающей.

def is_continuous_sequence(nums: list[int]) -> bool:
    return [
        i for i in range(nums[0], nums[-1] + 1)
        ] == nums if len(nums) > 1 else False


assert is_continuous_sequence([10, 11, 12, 13]) is True
assert is_continuous_sequence([-5, -4, -3]) is True
assert is_continuous_sequence([10, 11, 12, 14, 15]) is False
assert is_continuous_sequence([1, 2, 2, 3]) is False
assert is_continuous_sequence([7]) is False
assert is_continuous_sequence([]) is False
