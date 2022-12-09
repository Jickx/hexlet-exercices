import math


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


# BEGIN (write your solution here)
def get_x(point):
    return point["radius"] * math.cos(point["angle"])

def get_y(point):
    return point["radius"] * math.sin(point["angle"])
# END


x = 4
y = 8

# point хранит в себе данные в полярной системе координат
point = make_point(x, y)

# Здесь происходит преобразование из полярной в декартову
print(get_x(point))  # 4
print(get_y(point))  # 8
