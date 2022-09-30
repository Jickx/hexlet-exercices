# Напишите тесты для корзины интернет-магазина. Интерфейс:
# make_cart() – создаёт новую корзину (объект).
# add_item(good, count) – добавляет в корзину товары и их количество. Товар –
# это объект, у которого два свойства: name (имя) и price (стоимость).
# get_items() – возвращает список товаров в формате [{good, count},
# {good, count}, ...]
# get_cost() – возвращает стоимость корзины. Стоимость корзины высчитывается
# как сумма всех добавленных товаров с учётом их количества.
# get_count() – возвращает общее количество товаров в корзине.


from cart import get_implementations
from copy import deepcopy

# "right"
# "wrong1"
# "wrong2"
# "wrong3"

make_cart = get_implementations('right')


cart = make_cart()


def test_cart():
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert len(cart.get_items()) == 3
    assert cart.get_count() == 8
    assert cart.get_cost() == 45



