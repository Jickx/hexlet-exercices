# Транспонированием матрицы называется операция, при которой столбцы матрицы
# становятся строками, а строки становятся столбцами. Представим некую
# двумерную матрицу:
# 1 2 3
# 4 5 6
# 7 8 9

# После транспонирования матрица будет выглядеть так:
# 1 4 7
# 2 5 8
# 3 6 9


def transposed(matrix: list[list[int]]) -> list[list[int]]:
    return [list(i) for i in list(zip(*matrix))]


assert transposed([[1]]) == [[1]]
assert transposed([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert transposed([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
assert (transposed(transposed([[1, 2]])) == [[1, 2]]) is True
