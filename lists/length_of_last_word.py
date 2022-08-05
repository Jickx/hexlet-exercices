# Реализуйте функцию length_of_last_word(), которая возвращает длину
# последнего слова переданной на вход строки. Словом считается любая
# последовательность не содержащая пробелы, символы перевода строки \n
# и табуляции \t.


def length_of_last_word(words):
    words_list = words.split()
    if words and words_list:
        return len(words_list[-1])
    else:
        return 0


assert length_of_last_word('') == 0
assert length_of_last_word('man in Black') == 5
assert length_of_last_word('hello, world!     ') == 6
assert length_of_last_word('hello\t\nworld') == 5
assert length_of_last_word(' \t\n') == 0
