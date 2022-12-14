# Для задания цветов в HTML и CSS используются числа в шестнадцатеричной
# системе счисления. Чтобы не возникало путаницы в определении системы
# счисления, перед шестнадцатеричным числом ставят символ решетки #, например,
# #135278. Обозначение цвета (rrggbb) разбивается на три составляющие, где
# первые два символа обозначают красную компоненту цвета, два средних —
# зеленую, а два последних — синюю. Таким образом каждый из трех цветов —
# красный, зеленый и синий — может принимать значения от 00 до FF в
# шестнадцатеричной системе исчисления.

# При работе с цветами часто нужно получить отдельные значения красного,
# зеленого и синего (RGB) компонентов цвета в десятичной системе исчисления и
# наоборот. Реализуйте функции rgb2hex() и hex2rgb(), которые конвертируют
# цвета в соответствующие представления цвета.

# Функция rgb2hex() принимает 3 параметра (цветные компоненты) и возвращает
# строку. Функция должна работать как с позиционными, так и с именованными
# аргументами.

# Функция hex2rgb() возвращает словарь со значениями компонентов.


def rgb2hex(r=None, g=None, b=None) -> str:
    return '#' + ''.join(map(lambda x: f'{x:02x}', [r, g, b]))


def hex2rgb(hex: str) -> dict:
    hex = [hex[1:3], hex[3:5], hex[5:]]
    r, g, b = map(lambda x: int(x, 16), hex)
    return {'r': r, 'g': g, 'b': b}


assert rgb2hex(36, 171, 0) == '#24ab00'
assert rgb2hex(r=36, g=171, b=0) == '#24ab00'
assert (hex2rgb('#24ab00')) == {'r': 36, 'g': 171, 'b': 0}
