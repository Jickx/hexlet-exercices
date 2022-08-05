# Реализуйте функцию find_longest_length(), принимающую на вход строку и
# возвращающую длину максимальной последовательности из неповторяющихся
# символов. Подстрока может состоять из одного символа. Например в строке
# qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной
# будет weqrty, а её длина — 6 символов.

def find_longest_length(seq: str) -> str:
    longest_string = 0
    string = ''
    first_char_index = 0
    while longest_string < len(seq[first_char_index:]):
        for char in seq[first_char_index:]:
            if char not in string:
                string += char
            else:
                longest_string = max(longest_string, len(string))
                string = ''
                first_char_index += 1
                break
    return longest_string


assert find_longest_length('abcdeef') == 5
assert find_longest_length('jabjcdel') == 7
