# Реализуйте функцию build_itinerary(), которая выстраивает маршрут между
# городами и возвращает список городов, выстроенных в том же порядке,
# в котором они находятся на пути следования по маршруту.


def generate_parent_dict(subtree, parent=None, parent_dict={}):
    if len(subtree) == 2 and not isinstance(subtree[0], list):
        [city, path] = subtree
        parent_dict[city] = parent
        parent = city
        return generate_parent_dict(path, parent)
    for item in subtree:
        if len(item) == 1:
            [city] = item
            parent_dict[city] = parent
        else:
            generate_parent_dict(item, parent)
    return parent_dict


def generate_path_from_parent_dict(parent_dict, pathpoint):
    result = []

    def walk(parent_dict, curr_point=pathpoint):
        if not parent_dict[curr_point]:
            result.append(curr_point)
            return parent_dict[curr_point]
        result.append(curr_point)
        curr_point = parent_dict[curr_point]
        return walk(parent_dict, curr_point)

    walk(parent_dict)
    return result


def calculate_start_to_finish(start_point_path, finish_point_path):
    finish_point_path.reverse()
    for point in start_point_path:
        if point in finish_point_path:
            common_point = point
            break
    x = start_point_path[0:start_point_path.index(common_point)]
    y = finish_point_path[finish_point_path.index(common_point):]
    return x + y


def build_itinerary(tree, start_point, finish_point):
    parent_dict = generate_parent_dict(tree)
    start_point_path = generate_path_from_parent_dict(
        parent_dict,
        start_point
    )
    finish_point_path = generate_path_from_parent_dict(
        parent_dict,
        finish_point
    )

    return calculate_start_to_finish(
        start_point_path,
        finish_point_path
    )


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

print(build_itinerary(tree, 'Borisovka', 'Kurchatov'))
# ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
