def build_city_routes(tree, routes):
    if len(tree) == 1:
        city = tree[0]
        routes[city] = []
        return city

    city, neighbours = tree
    routes[city] = []

    for tree in neighbours:
        neighbour = build_city_routes(tree, routes)
        routes[city].append(neighbour)
        routes[neighbour].append(city)
    return city


def search_way(start_city, finish_city, path, routes):
    if start_city == finish_city:
        return path + [finish_city]

    for city in routes[start_city]:
        if city in path:
            continue
        rest = search_way(
            city, finish_city, path + [start_city], routes
        )
        if rest:
            return rest


def build_itinerary(tree, start_city, finish_city):
    routes = {}
    build_city_routes(tree, routes)
    print('\n')
    print(routes)
    print('\n')
    return search_way(start_city, finish_city, [], routes)


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