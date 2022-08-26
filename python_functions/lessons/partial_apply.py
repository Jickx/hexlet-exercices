# В этом упражнении вам нужно будет реализовать две функции высшего порядка,
# возвращающие замыкания: partial_apply() и flip().

# partial_apply() принимает функцию от двух аргументов и первый аргумент для
# неё, а возвращает замыкание — функцию, которая примет второй аргумент и
# наконец применит замкнутую функцию к обоим аргументам (и вернёт результат).

def partial_apply(function, arg1):
    def inner(arg2):
        return function(arg1, arg2)
    return inner


def greet(name, surname):
    return f'Hello, {name} {surname}!'


f = partial_apply(greet, 'Dorian')
assert f('Grey') == 'Hello, Dorian Grey!'

# Функция flip() принимает в качестве единственного аргумента функцию от двух
# аргументов. Возвращаемое замыкание должно также принять два аргумента, а
# затем применить к ним замкнутую функцию, но аргументы подставить в обратном
# порядке. Таким образом flip() как бы "переворачивает" ("flips") исходную
# функцию.


def flip(function):
    def inner(arg1, arg2):
        return function(arg2, arg1)
    return inner


def greet(name, surname):
    return f'Hello, {name} {surname}!'


f = flip(greet)
assert f('Christian', 'Teodor') == 'Hello, Teodor Christian!'
