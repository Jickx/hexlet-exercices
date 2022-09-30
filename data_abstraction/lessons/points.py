# Реализуйте функцию, которая находит точку посередине между двумя указанными
# точками:

def get_mid_point(p1, p2):
    x = (p1['x'] + p2['x']) / 2
    y = (p1['y'] + p2['y']) / 2
    return {'x': x, 'y': y}


point1 = {'x': 0, 'y': 0}
point2 = {'x': 4, 'y': 4}
assert get_mid_point(point1, point2) == {'x': 2, 'y': 2}
