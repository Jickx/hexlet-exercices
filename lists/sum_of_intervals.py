# Реализуйте функцию sum_of_intervals(), которая принимает на вход список
# интервалов и возвращает сумму всех длин интервалов. В данной задаче
# используются только интервалы целых чисел от 1 до ∞ , которые представлены в
# виде списков. Первое значение интервала всегда будет меньше, чем второе
# значение. Например, длина интервала [1, 5] равна 4, а длина интервала [5, 5]
# равна 0. Пересекающиеся интервалы должны учитываться только один раз.


def merge_intervals(intervals: list[list]) -> int:
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])
    return output


def sum_of_intervals(intervals: list[list]) -> int:
    output = 0
    intervals = merge_intervals(intervals)
    for interval in intervals:
        length = interval[-1] - interval[0]
        output += length
    return output


assert sum_of_intervals([
    [1, 1],
]) == 0
assert sum_of_intervals([
    [1, 2],
    [50, 100],
    [60, 70],
]) == 51
assert sum_of_intervals([
    [1, 2],
    [5, 10],
]) == 6

assert sum_of_intervals([
    [7, 10],
    [1, 4],
    [2, 5],
]) == 7
