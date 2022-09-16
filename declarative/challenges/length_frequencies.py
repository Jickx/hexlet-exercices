# Вам необходимо реализовать функцию length_frequencies(), которая принимает
# последовательность (iterable) слов (строк) в качестве единственного аргумента
# и возвращает словарь, ключами которого выступают длины слов, а значениями —
# количество слов соответствующей длины.
# Это задание можно выполнить в процедурном стиле с помощью defaultdict или
# dict.setdefault, однако попробуйте описать декларативное решение с
# использованием comprehensions. Возможно, вам пригодится функция
# itertools.groupby().


from collections import defaultdict


def length_frequencies(words: list[str]) -> dict:
    result = defaultdict(int)
    for word in words:
        result[len(word)] += 1
    return dict(result)


print(length_frequencies([]))  # {}
print(length_frequencies(['abcde']))  # {5: 1}
print(length_frequencies(['a', 'b', 'c']))  # {1: 3}
print(length_frequencies('Use the Force, Luke!'.split()))  # {3: 2, 5: 1, 6: 1}
