# Реализуйте функцию build_itinerary(), которая выстраивает маршрут между
# городами и возвращает список городов, выстроенных в том же порядке,
# в котором они находятся на пути следования по маршруту.

from copy import deepcopy


def build_itinerary(tree, start, finish):
    result = []
    parent_city_list = []


    def walk(subtree, start):
        found = True
        if len(subtree) == 2 and not isinstance(subtree[0], list):
            [city, route] = subtree
            parent_city_list.append(city)
            return walk(route, start)
        if found is not True:
            parent_city_list.pop()
            found = False
        for city in subtree:
            if len(city) != 1:
                walk(city, start)
            elif city == [start]:
                found = True
                result.append(deepcopy(parent_city_list))
                result.append(city)
        map(walk, subtree)
        print(f'Parent city list: {parent_city_list}')
        return parent_city_list
    walk(tree, start)
    return result



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

build_itinerary(tree, 'Borisovka', 'Kurchatov')
# ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
