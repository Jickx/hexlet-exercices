def is_perfect(number):
    number_list = [i for i in range(1, number) if number % i == 0]
    return number_list or False


assert is_perfect(6) == [1, 2, 3]
assert is_perfect(28) == [1, 2, 4, 7, 14]