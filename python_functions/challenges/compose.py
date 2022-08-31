# С точки зрения математики, композиция функций f и g — новая функция
# z(x) = f(g(x)).
# Реализуйте функцию compose(), которая принимает на вход две других
# одноаргументных функции и возвращает новую функцию. Эта новая функция также
# должна принимать один аргумент и применять к нему исходные функции в нужном
# порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).

def compose(f, g):
    def inner(x):
        return f(g(x))
    return inner


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


print(compose(mul3, add5)(1))
# 18
print(compose(add5, mul3)(1))
# 8
print(compose(mul3, str)(1))
# '111'
print(compose(str, mul3)(1))
# '3'
