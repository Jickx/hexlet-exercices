# В этот раз вы снова будете реализовывать мемоизирующий декоратор
# "memoizing". Но на этот раз декоратор должен принимать аргумент, задающий
# максимальное количество запоминаемых значений. При превышении количества
# запомненных значений лишние должны быть отброшены, причём сначала — самые
# старые!

# Напоминаю, мемоизируемые функции считать численными функциями одного
# аргумента. И не забудьте про functools.wraps!

from functools import wraps


def memoizing(limit):
    def wrapper(function):
        memory = {}
        order = []

        @wraps(function)
        def inner(number):
            memoizing_result = memory.get(number)
            if memoizing_result is None:
                memoizing_result = function(number)
                memory[number] = memoizing_result
                order.append(number)
            if len(order) > limit:
                oldest_element = order.pop(0)
                memory.pop(oldest_element)
            return memoizing_result
        return inner
    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
# => Calculating...
# 10
print(f(1))  # будет "вспомнено"
# 10
print(f(2))
# => Calculating...
# 20
print(f(3))
# => Calculating...
# 30
print(f(4))  # вытеснит запомненный результат для "1"
# => Calculating...
# 40
print(f(1))  # будет перевычислено
# => Calculating...
# 10
