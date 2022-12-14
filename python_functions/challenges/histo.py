# Гистограмма — это графическое представление данных в виде столбцов или
# колонок.
# Реализуйте функцию histo(), которая принимает на вход список или кортеж с
# числами и возвращает гистограмму в виде строки, столбцы гистограммы в ней
# разделены символами \n. Каждый столбец отображает количество вхождений числа
# в список: графически с помощью заданных символов и в виде числового
# значения, за исключением случаев, когда количество равно нулю.

# Необязательные параметры:
# min_value — определяет минимальное значение, для которого рисуется
# гистограмма. По умолчанию не задан, то есть верхний стобец в гистограмме
# соответствует минимальному из переданных чисел.

# max_value — определяет максимальное значение, для которого рисуется
# гистограмма. По умолчанию не задан, то есть нижний столбец в гистограмме
# соответствует максимальному из переданных чисел.

# bar_char — символ, с помощью которого создаются столбцы в гистограмме. По
# умолчанию — #.

from collections import Counter


def histo(samples: list[int], min_value=None,
          max_value=None, bar_char='#') -> str:
    barchart = []
    barchart_ctr = dict(Counter(samples))
    if not min_value:
        min_value = min(samples)
    if not max_value:
        max_value = max(samples)
    for value in range(min_value, max_value + 1):
        quantity = barchart_ctr.get(value, 0)
        line = f'{value}|{bar_char * quantity}'
        if quantity:
            line += f' {quantity}'
        barchart.append(line)
    barchart = '\n'.join(barchart)
    return barchart


print(histo([1, 1, 3, 4, 5]))
# => 1|## 2
# => 2|
# => 3|# 1
# => 4|# 1
# => 5|# 1
print(histo([1, 1, 3, 4, 5], bar_char='*'))
# => 1|** 2
# => 2|
# => 3|* 1
# => 4|* 1
# => 5|* 1
print(histo([1, 1, 3, 4, 5], min_value=3, max_value=4))
# => 3|# 1
# => 4|# 1
print(histo([], min_value=1, max_value=5))
# => 1|
# => 2|
# => 3|
# => 4|
# => 5|
