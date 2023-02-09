# Реализуйте функцию build_itinerary(), которая выстраивает маршрут между
# городами и возвращает список городов, выстроенных в том же порядке,
# в котором они находятся на пути следования по маршруту.

from copy import deepcopy


def build_itinerary(tree, start_point, finish_point):
    result = []
    parent_dict = {}

    def get_route_from_parent_dict(parent_dict):
        pass


    def walk(subtree, point, parent=None):
        if len(subtree) == 2 and not isinstance(subtree[0], list):
            [city, route] = subtree
            parent_dict[city] = parent
            parent = city
            return walk(route, point, parent)
        for item in subtree:
            if len(item) != 1:
                walk(item, point, parent)
            elif item == [point]:
                result.append(parent_dict)
                result.append(item)
        return result
    start_path = deepcopy(walk(tree, start_point))
    parent_dict.clear()
    result.clear()
    finish_path = deepcopy(walk(tree, finish_point))
    return start_path, finish_path



tree = ['Moscow', [
    ['Smolensk'],
    ['Yaroslavl'],
    ['Voronezh', [
        ['Liski'],
        ['Boguchar'],
        ['Kursk', [
            ['Belgorod', [
                ['Borisovka'],
            ]],
            ['Kurchatov'],
        ]],
    ]],
    ['Ivanovo', [
        ['Kostroma'], ['Kineshma'],
    ]],
    ['Vladimir'],
    ['Tver', [
        ['Klin'], ['Dubna'], ['Rzhev'],
    ]],
]]

print(build_itinerary(tree, 'Dubna', 'Kostroma'))
# ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']

# build_itinerary(tree, 'Borisovka', 'Kurchatov')
# ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
