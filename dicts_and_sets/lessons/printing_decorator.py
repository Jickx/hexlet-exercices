def printing(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f'result: {result}')
        return result
    return inner


@printing
def add_one(x):
    return x + 1


add_one(10)
