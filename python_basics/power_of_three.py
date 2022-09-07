def is_power_of_three(x):
    while x % 3 == 0:
        x /= 3
    return x == 1

print(is_power_of_three(9))
    