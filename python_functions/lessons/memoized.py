# Вам предстоит реализовать декоратор, добавляющий функции мемоизацию.
# Мемоизация — это запоминание уже вычисленных результатов для уже однажды
# встреченных аргументов.
# Для простоты будем считать, что мемоизироваться будут численные функции
# одного аргумента (аргумент — число, результат — тоже число).


def memoized(function):
    memory = {}

    def inner(num):
        memoized_result = memory.get(num)
        if memoized_result is None:
            memoized_result = function(num)
            memory[num] = memoized_result
        return memoized_result
    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
# => Calculating...
# 10
print(f(1))
# 10
print(f(42))
# => Calculating...
# 420
print(f(42))
# 420
print(f(1))
# 10
