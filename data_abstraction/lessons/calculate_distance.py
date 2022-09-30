# Реализуйте функцию calculate_distance(), которая находит расстояние между
# двумя точками на плоскости:

from math import sqrt


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))


assert calculate_distance([0, 0], [3, 4]) == 5
assert calculate_distance([-1, -4], [-1, -10]) == 6
assert calculate_distance([1, 10], [1, 3]) == 7
