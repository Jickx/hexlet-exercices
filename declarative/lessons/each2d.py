# Вам предстоит реализовать три функции, каждая из которых будет работать с
# двухмерной матрицей, то есть со списком списков (итератором итераторов):

# each2d(test, matrix) должна проверить, что каждый элемент матрицы matrix
# удовлетворяет предикату test, и вернуть False, если хотя бы для одного
# элемента test вернул False. В противном случае функция должна возвращать
# True.


def each2d(test, matrix):
    return all(map(test, (item for item in
                          (item for sub_list in matrix for item in sub_list))))


# some2d(test, matrix) должна проверить, удовлетворяет ли предикату test хотя
# бы один элемент матрицы matrix. Как только test возвращает True для
# какого-либо элемента, функция должна вернуть True, в противном случае
# (если ни один элемент проверку не прошел) нужно вернуть False.


def some2d(test, matrix):
    return any(map(test, (item for item in
                          (item for sub_list in matrix for item in sub_list))))


# sum2d(test, matrix) должна возвращать сумму всех элементов матрицы matrix,
# удовлетворяющих предикату test.


def sum2d(test, matrix):
    return sum(
        item for item in (item for sub_list in matrix for item in sub_list) if
        test(item))


# Внимание, первые две функции не должны выполнять лишней работы: обход матрицы
# должен прерываться, как только результат становится ясен.


def is_int(x):
    return isinstance(x, int)


assert each2d(is_int, [[1, 2], [3, 4]]) is True
assert each2d(is_int, [[1, None], [3, 4]]) is False
# В пустой матрице нет ни одного элемента, который бы завалил тест
assert each2d(is_int, []) is True

assert some2d(is_int, [[None, "foo"], [(), {}]]) is False
assert some2d(is_int, [[None, "foo"], [0, {}]]) is True
# В пустой матрице нет ни одного элемента, который бы прошел тест
assert some2d(is_int, []) is False

print(sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]))  # 111
