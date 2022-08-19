# Вам нужно реализовать функцию greet(), которая должна принимать несколько
# имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).

def greet(name, *args):
    return f"Hello, {' and '.join([name, *args])}!"


assert greet('Bob') == 'Hello, Bob!'
assert greet('Moe', 'Mary') == 'Hello, Moe and Mary!'
assert greet(*'ABC') == 'Hello, A and B and C!'
