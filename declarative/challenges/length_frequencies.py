# Вам необходимо реализовать функцию length_frequencies(), которая принимает
# последовательность (iterable) слов (строк) в качестве единственного аргумента
# и возвращает словарь, ключами которого выступают длины слов, а значениями —
# количество слов соответствующей длины.
# Это задание можно выполнить в процедурном стиле с помощью defaultdict или
# dict.setdefault, однако попробуйте описать декларативное решение с
# использованием comprehensions. Возможно, вам пригодится функция
# itertools.groupby().

from itertools import groupby


def length_frequencies(words: list[str]) -> dict:
    return {k: len(list(g)) for k, g in
            groupby(sorted([len(i) for i in words]))}


assert length_frequencies([]) == {}
assert length_frequencies(['abcde']) == {5: 1}
assert length_frequencies(['a', 'b', 'c']) == {1: 3}
assert length_frequencies('Use the Force, Luke!'.split()) == {3: 2, 5: 1, 6: 1}
assert length_frequencies(
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.""".split(),
) == {
           2: 13,
           3: 5,
           4: 9,
           5: 12,
           6: 7,
           7: 9,
           8: 3,
           9: 5,
           10: 3,
           11: 1,
           12: 1,
           13: 1,
       }
