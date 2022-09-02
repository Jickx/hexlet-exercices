# Задача заключается в том, что нужно реализовать функцию enlarge(), которая
# увеличивает переданное "изображение" в два раза: каждый "пиксель"
# удваивается по горизонтали и вертикали. Изображением служит список строк, а
# пиксели в нём — символы строк.

from functools import reduce
from operator import add

curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731

glider = [' * ', '  *', '***']

concat = curry(reduce)(add)
concat_map = compose(compose(concat))(curry(map))

enlarge = concat_map(compose(pair)(concat_map(dup)))


def display(image):
    for line in image:
        print(line)


display(glider)
# =>  *
# =>   *
# => ***
display(enlarge(glider))
# =>   **
# =>   **
# =>     **
# =>     **
# => ******
# => ******
