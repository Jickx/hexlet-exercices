# Для записи цифр римляне использовали буквы латинского алфавита: I, V, X, L,
# C, D, M. Например:
# 1 обозначалась с помощью буквы I
# 10 с помощью Х
# 7 с помощью VII
# Число 2020 в римской записи — это MMXX (2000 = MM, 20 = XX).

# Реализуйте функцию to_roman(), которая переводит арабские числа в римские.
# Функция принимает на вход целое число из диапазона от 1 до 3000, а
# возвращает строку с римским представлением этого числа.

# Реализуйте функцию to_arabic(), которая переводит число в римской записи в
# число, записанное арабскими цифрами. Если переданное римское число не
# корректно, то функция должна вернуть значение False.

NUMERALS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def to_roman(num: int) -> str:
    quantity = 0
    result = ''
    for roman, arabic in NUMERALS.items():
        if num >= arabic:
            quantity = num // arabic
            result += quantity * str(roman)
            num -= arabic * quantity
        if num == 0:
            return result


def get_num_list(num: str) -> list:
    """"get list with correct roman numbers"""
    i = 0
    output = []
    while i < len(num):
        if num[i:i + 2] in NUMERALS:
            output.append(num[i:i + 2])
            i += 2
        elif num[i] in NUMERALS:
            output.append(num[i])
            i += 1
        else:
            return False
    return output


def to_arabic(num: str) -> int:
    num_list = get_num_list(num)
    if not num_list:
        return False
    output = 0
    for i in num_list:
        output += NUMERALS[i]
    if num == to_roman(output):
        return output
    else:
        return False


assert to_roman(0) == ''
assert to_roman(1) == 'I'
assert to_roman(2) == 'II'
assert to_roman(4) == 'IV'
assert to_roman(5) == 'V'
assert to_roman(6) == 'VI'
assert to_roman(27) == 'XXVII'
assert to_roman(48) == 'XLVIII'
assert to_roman(59) == 'LIX'
assert to_roman(93) == 'XCIII'
assert to_roman(141) == 'CXLI'
assert to_roman(163) == 'CLXIII'
assert to_roman(402) == 'CDII'
assert to_roman(575) == 'DLXXV'
assert to_roman(911) == 'CMXI'
assert to_roman(1024) == 'MXXIV'
assert to_roman(2020) == 'MMXX'
assert to_roman(3000) == 'MMM'

assert to_arabic('') == 0
assert to_arabic('I') == 1
assert to_arabic('II') == 2
assert to_arabic('IV') == 4
assert to_arabic('V') == 5
assert to_arabic('VI') == 6
assert to_arabic('XXVII') == 27
assert to_arabic('XLVIII') == 48
assert to_arabic('LIX') == 59
assert to_arabic('XCIII') == 93
assert to_arabic('CXLI') == 141
assert to_arabic('CLXIII') == 163
assert to_arabic('CDII') == 402
assert to_arabic('DLXXV') == 575
assert to_arabic('CMXI') == 911
assert to_arabic('MXXIV') == 1024
assert to_arabic('MMXX') == 2020
assert to_arabic('MMM') == 3000
assert to_arabic('IIII') is False
assert to_arabic('VX') is False
