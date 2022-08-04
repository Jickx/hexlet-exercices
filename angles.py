# Напишите функцию diff, которая принимает два угла (int)
# и возвращает наименьшую разницу между ними.

def diff(x, y):
    if abs(x) > 360:
        x = x % 360
    if abs(y) > 360:
        y = y % 360
    angle = abs(x - y)
    return angle if 360 - angle > angle else 360 - angle


print(diff(-100, 200))
