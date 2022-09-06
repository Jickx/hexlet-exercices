# Реализуйте функцию filter_anagrams(), которая находит все слова-анаграммы.
# Функция принимает исходное слово и последовательность (iterable) слов для
# проверки, а возвращает последовательность анаграмм.
# Я использовал в абзаце "слова" только для краткости. Строго говоря, ваша
# функция должна уметь находить анаграммы любых последовательностей, в том
# числе списков и кортежей. То есть решение должно быть максимально общим.

def sorted_anagram(anagram):
    return sorted(anagram)


def filter_anagrams(anagram: str, sequence: any) -> any:
    return filter(
        lambda item: sorted_anagram(item) == sorted(anagram),
        sequence)


assert list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) == [
    'aabb', 'bbaa']
assert list(filter_anagrams('racer', [
    'crazer', 'carer', 'racar', 'caers', 'racer'])) == [
    'carer', 'racer']
assert list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer'])) == []
assert list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]])) == [
    [2, 1], [1, 2]]
