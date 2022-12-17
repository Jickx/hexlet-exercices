# Реализуйте абстракцию для работы с рациональными числами включающую в себя
# следующие функции:
# Конструктор make — принимает на вход числитель и знаменатель, возвращает дробь.
# Селектор get_numer — возвращает числитель
# Селектор get_denom — возвращает знаменатель
# Сложение add — складывает переданные дроби
# Вычитание sub — находит разность между двумя дробями
# Не забудьте реализовать нормализацию дробей удобным для вас способом.

from math import gcd


def make(numer, denumer):
    gcd_number = gcd(numer, denumer)
    return {
        "numer": int(numer / gcd_number),
        "denumer": int(denumer / gcd_number)
    }


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denumer"]


def add(rat1, rat2):
    numer1 = get_numer(rat1)
    numer2 = get_numer(rat2)
    denumer1 = get_denom(rat1)
    denumer2 = get_denom(rat2)
    if denumer1 == denumer2:
        return make(numer1 + numer2, denumer1)
    return make(
        (numer1 * denumer2) + (numer2 * denumer1),
        (denumer1 * denumer2)
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    numer2 = get_numer(rat2)
    denumer1 = get_denom(rat1)
    denumer2 = get_denom(rat2)
    if denumer1 == denumer2:
        return make(numer1 - numer2, denumer1)
    return make(
        (numer1 * denumer2) - (numer2 * denumer1),
        (denumer1 * denumer2)
    )


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


rat1 = make(3, 9)
rat2 = make(10, 3)
rat3 = make(-4, 16)
rat4 = make(12, 5)

print(get_numer(rat1)) # 1
print(get_denom(rat1)) # 3
print(add(rat1, rat2)) # make(11, 3)
print(sub(rat1, rat2)) # make(-3, 1)







