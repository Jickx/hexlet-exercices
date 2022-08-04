# Вес Хэмминга это количество единиц в двоичном представлении числа.
# Реализуйте функцию hamming_weight, которая считает вес Хэмминга.

def hamming_weight(num):
    return sum([int(i) for i in bin(num)[2:]])


assert hamming_weight(0) == 0
assert hamming_weight(4) == 1
assert hamming_weight(101) == 4
