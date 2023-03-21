# Реализуйте декоратор suppress ("подавлять"), который должен перехватывать
# заданное исключение (одно или несколько), если таковое возникнет при вызове
# оборачиваемой функции, и возвращать вместо ошибки заданное значение
# (keyword-only аргумент "or_return", значение по умолчанию — None).


from functools import wraps


def suppress(exception_name, or_return=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_name:
                return or_return
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


print(foo())  # 42


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


print(get_item(7, "foo") is None)  # True
print(get_item('a', {}) is None)  # True


def walk(path, structure):
    """Walk down to structure using path."""
    if not path:
        return structure
    key, *rest_path = path
    return walk(rest_path, structure[key])


assert walk([0], 'Cat') == 'C'
assert walk(['a', 1], {'a': ('foo', 'bar')}) == 'bar'
assert walk(['x', 1, 0], {'x': ('foo', 'bar')}) == 'b'


@suppress(ZeroDivisionError, or_return=0)
def safe_div(a, *, b):
    return a // b


assert safe_div(10, b=3) == 3
assert safe_div(10, b=0) == 0

safe_walk = suppress((KeyError, IndexError))(walk)

assert safe_walk([1], "") is None
assert safe_walk(['a'], {}) is None
assert safe_walk([0, 0, 1], (("?", 100), 200)) is None
