# Реализуйте абстракцию (набор функций) для работы с прямоугольниками, стороны
# которого всегда параллельны осям. Прямоугольник может располагаться в любом
# месте координатной плоскости.

# При такой постановке достаточно знать только три параметра для однозначного
# задания прямоугольника на плоскости: координаты левой-верхней точки, ширину
# и высоту. Зная их, мы всегда можем построить прямоугольник одним единственным
# способом.

from points import get_quadrant, get_x, get_y, make_decart_point


def make_rectangle(point, width, height):
    return {
        "point": point,
        "width": width,
        "height": height
    }


def get_start_point(rectangle):
    return rectangle["point"]


def get_width(rectangle):
    return rectangle["width"]


def get_height(rectangle):
    return rectangle["height"]


def check_quadrant(point):
    if get_quadrant(point):
        return True
    else:
        return False


def contains_origin(rectangle):
    start_point = get_start_point(rectangle)
    width = get_width(rectangle)
    height = get_height(rectangle)
    x, y = get_x(start_point), get_y(start_point)
    a = start_point
    b = make_decart_point(x + width, y)
    c = make_decart_point(x + width, y - height)
    d = make_decart_point(x, y - height)

    print(a, b, c, d)

    quadrant_a = get_quadrant(a)
    quadrant_b = get_quadrant(b)
    quadrant_c = get_quadrant(c)
    quadrant_d = get_quadrant(d)
    quadrants_list = [quadrant_a, quadrant_b, quadrant_c, quadrant_d]

    if check_quadrant(a) and check_quadrant(b) and \
            check_quadrant(c) and check_quadrant(d):
        if len(set(quadrants_list)) == len(quadrants_list):
            return True
    return False

print(contains_origin({'height': 2, 'point': {'x': -4, 'y': 3}, 'width': 5}))