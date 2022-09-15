# Вам предстоит потренироваться в написании генераторных функций и написать три
# штуки:

# my_map(f, xs), которая должна работать как упрощенная версия map()
def my_map(f, xs) -> iter:
    return (f(i) for i in xs)


# my_filter(f, xs), упрощенный вариант filter()
def my_filter(f, xs) -> iter:
    return (i for i in xs if f(i))


# replicate_each(n, xs) должен для каждого элемента итератора xs выдавать на
# выход по n копий этого элемента
def replicate_each(n, xs):
    return (item for item in xs for _ in range(n))


assert list(my_map(abs, [-1, 2, -3])) == [1, 2, 3]
assert list(my_filter(lambda x: x % 2 == 1, range(10))) == [1, 3, 5, 7, 9]
assert list(replicate_each(1, [1, 'a'])) == [1, 'a']
assert list(replicate_each(3, [1, 'a'])) == [1, 1, 1, 'a', 'a', 'a']
assert list(replicate_each(0, [1, 'a'])) == []
