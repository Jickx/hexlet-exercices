def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(number):
    for i in range(10):
        if number == 1:
            return True
        number = sum_of_square_digits(number)
    return False

print(is_happy_number(7))