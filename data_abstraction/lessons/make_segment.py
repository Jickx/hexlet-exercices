# Отрезок — еще один графический примитив. В коде описывается парой точек, одна
# из которых — начало отрезка, другая — конец. Обычный отрезок не имеет
# направления, поэтому вы сами вольны выбирать то, какую точку считать началом,
# а какую концом.
# В этом задании подразумевается, что вы уже понимаете принцип построения
# абстракции и способны самостоятельно принять решение о том, как она будет
# реализована. Напомню, что сделать это можно разными способами и нет одного
# правильного.
# Реализуйте указанные ниже функции:
# make_segment() — принимает на вход две точки и возвращает отрезок.
# get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку,
# находящуюся на середине отрезка.
# get_begin_point() — принимает на вход отрезок и возвращает точку начала
# отрезка.
# get_end_point() — принимает на вход отрезок и возвращает точку конца отрезка.

from points import get_x, get_y, make_decart_point


def make_segment(start, end):
    return {'start': start, 'end': end}


def get_mid_point_of_segment(seg):
    x = (get_x(seg['start']) + get_x(seg['end'])) / 2
    y = (get_y(seg['start']) + get_y(seg['end'])) / 2
    return make_decart_point(x, y)


def get_begin_point(seg):
    return seg['start']


def get_end_point(seg):
    return seg['end']


begin_point = make_decart_point(4, 2)
end_point = make_decart_point(0, 0)
segment = make_segment(begin_point, end_point)
assert get_begin_point(segment) == begin_point
assert get_end_point(segment) == end_point
assert make_decart_point(2, 1) == get_mid_point_of_segment(segment)

segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)
