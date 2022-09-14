# Вам необходимо реализовать функцию number_of_unique_letters(), которая должна
# подсчитывать количество уникальных букв в строке-аргументе без учёта регистра

def number_of_unique_letters(some_string: str) -> int:
    return len({i.lower() for i in some_string if i.isalpha()})


assert number_of_unique_letters("") == 0
assert number_of_unique_letters("abc") == 3
assert number_of_unique_letters("A-a-a-a-a-a!") == 1
assert number_of_unique_letters("\\(O_o)/") == 1
assert number_of_unique_letters("AaBbCcDd") == 4
