# Реализуйте функцию-предикат scrabble, которая принимает на вход два
# параметра: набор символов (строку) и слово, и проверяет, можно ли из
# переданного набора составить это слово. В результате вызова функция
# возвращает True или False.
# При проверке учитывается количество символов, которые нужны для составления
# слова, и не учитывается их регистр.

from collections import Counter


def scrabble(letters: str, word: str) -> bool:
    letters = Counter(letters.lower())
    for char in word.lower():
        if letters[char] > 0:
            letters[char] -= 1
        else:
            return False
    return True


assert scrabble('begsdhhtsexoult', 'hexlet') is True
assert scrabble('rkqodlw', 'world') is True
assert scrabble('begsdhhtsexoult', 'hexlet') is True
assert scrabble('katas', 'steak') is False
assert scrabble('scriptjava', 'javascript') is True
assert scrabble('scriptingjava', 'javascript') is True
assert scrabble('scriptjavest', 'javascript') is False
assert scrabble('', 'hexlet') is False
assert scrabble('scriptingjava', 'JavaScript') is True
