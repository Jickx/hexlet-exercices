# Вам предстоит реализовать два решения одной и той же задачи —
# функциональное и процедурное.

# Задача состоит в том, чтобы для входного списка списков получить список
# нечётных по порядку списков (первый, третий и так далее), оставив в каждом
# только нечётные по порядку элементы. Например, для из списка [[1, 2, 3],
# [4, 5, 6], [7, 8, 9]] должен получиться список [[1, 3], [7, 9]].

# При этом функциональное решение должно вычислять новый список списков на
# основе оригинального. Оригинальный же список должен оставаться неизменным. У
# вас должна получиться функция odds_from_odds():

def odds(list_of_lists: list[list]) -> list:
    find_odds = lambda x: x[0] % 2 == 0  # noqa
    pair = lambda x: x[1]  # noqa
    return list(map(pair, filter(find_odds, enumerate(list_of_lists))))


def odds_from_odds(list_of_lists: list[list]) -> list:
    return list(map(odds, odds(list_of_lists)))


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert odds_from_odds(lst) == [[1, 3], [7, 9]]
print(lst)  # оригинал не изменился!
# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert odds_from_odds([]) == []  # пустой список не должен быть проблемой
assert odds_from_odds([[]]) == [[]]  # как и список пустых списков

# Процедурное решение должно изменить список-аргумент по месту, а не
# возвращать его новую версию. Постарайтесь обойтись без создания
# вспомогательных структур, в том числе и для обработки вложенных списков. У
# вас должна получиться функция keep_odds_from_odds():


def keep_odd(some_list) -> None:
    index = 0
    for i in range(len(some_list)):
        if i % 2 != 0:
            some_list.pop(index)
        else:
            index += 1


def keep_odds_from_odds(list_of_lists):
    keep_odd(list_of_lists)
    for lists in list_of_lists:
        keep_odd(lists)


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
keep_odds_from_odds(l)  # процедура ничего не возвращает
print(l)  # но меняет аргумент
# => [[1, 3], [7, 9]]
keep_odds_from_odds(l)
print(l)
# => [[1]]
keep_odds_from_odds(l)
print(l)  # тут уже ничего чётного не осталось, поэтому никаких изменений нет
# => [[1]]
keep_odds_from_odds([])  # пустой список не должен быть проблемой
keep_odds_from_odds([[]])  # как и список пустых списков
