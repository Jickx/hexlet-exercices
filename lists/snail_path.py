# Матрицу можно представить в виде двумерного списка. Например, список
# [[1, 2, 3, 4], [5, 6, 7, 8]] — это отображение матрицы:

# 1 2 3 4
# 5 6 7 8

# Реализуйте функцию snail_path(), которая принимает на вход матрицу и
# возвращает список элементов матрицы по порядку следования от левого верхнего
# элемента по часовой стрелке к внутреннему.

def snail_path(items: list[list]) -> list:
    if items == [] or items == [[]]:
        return None
    row = 0
    column = 0
    number_of_items = len(items) * len(items[0])
    output = [items[0][0]]
    items[row][column] = 100500
    column += 1
    while len(output) < number_of_items:
        while True:
            if column == len(items[0]) or items[row][column] == 100500:
                column -= 1
                row += 1
                break
            if items[row][column] != 100500:
                output.append(items[row][column])
                items[row][column] = 100500
                column += 1
        while True:
            if row == len(items) or items[row][column] == 100500:
                row -= 1
                column -= 1
                break
            if items[row][column] != 100500:
                output.append(items[row][column])
                items[row][column] = 100500
                row += 1
        while True:
            if column == len(items[0]) or items[row][column] == 100500:
                column += 1
                row -= 1
                break
            if items[row][column] != 100500:
                output.append(items[row][column])
                items[row][column] = 100500
                column -= 1
        while True:
            if row == len(items) or items[row][column] == 100500:
                row += 1
                column += 1
                break
            if items[row][column] != 100500:
                output.append(items[row][column])
                items[row][column] = 100500
                row -= 1
    return output


assert not snail_path([])

assert not snail_path([[]])

assert snail_path([[0]]) == [0]

assert snail_path([[1, 2, 3]]) == [1, 2, 3]

assert snail_path([[1], [2], [3], [4]]) == [1, 2, 3, 4]

assert snail_path([
    [1, 2],
    [3, 4],
]) == [1, 2, 4, 3]

assert snail_path([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

assert snail_path([
    [None, 0, True],
    [-1, '', False],
    [[], 'foo', object],
]) == [None, 0, True, False, object, 'foo', [], -1, '']

assert snail_path([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
