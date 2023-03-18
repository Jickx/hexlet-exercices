# В этот раз вы снова будете реализовывать мемоизирующий декоратор
# "memoizing". Но на этот раз декоратор должен принимать аргумент, задающий
# максимальное количество запоминаемых значений. При превышении количества
# запомненных значений лишние должны быть отброшены, причём сначала — самые
# старые!

# Напоминаю, мемоизируемые функции считать численными функциями одного
# аргумента. И не забудьте про functools.wraps!

from functools import wraps


def memoizing(num_of_mem_slots):

    def wrapper(func):
        memory = {}
        slots = []

        @wraps(func)
        def inner(num):
            if num in memory:
                return memory[num]
            res = func(num)
            memory[num] = res
            slots.append(num)
            if len(slots) > num_of_mem_slots:
                del_slot = slots.pop(0)
                del memory[del_slot]
            return res
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
