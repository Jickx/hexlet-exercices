# В этом упражнении вам нужно будет, используя функцию rgb(), реализовать
# функцию get_colors(), которая должна вернуть словарь цветов. В словаре
# должны присутствовать ключи 'red', 'green', 'blue'. Каждому ключу должен
# соответствовать результат вызова функции rgb() со значением 255 для
# соответствующего ключу аргумента. Для построения каждого цвета используйте
# только один аргумент!

def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255),
        }


colors = get_colors()
assert set(colors.keys()) == {'red', 'green', 'blue'}
assert colors['red'] == rgb(red=255)
assert colors['green'] == rgb(green=255)
assert colors['blue'] == rgb(blue=255)
