# Реализуйте функцию transform(), которая строит дерево относительно заданного
# корневого узла.
# Функция на вход принимает 2 аргумента:
# - исходное дерево
# - узел, от которого будет построено новое дерево.
# Функция должна возвращать новое дерево с сохранёнными связями между узлами,
# в котором переданный узел является корневым.


def build_routes(tree, routes):
    if len(tree) == 1:
        item = tree[0]
        routes[item] = []
        return item

    item, neighbours = tree
    routes[item] = []

    for tree in neighbours:
        neighbour = build_routes(tree, routes)
        routes[item].append(neighbour)
        routes[neighbour].append(item)
    return item


def build_tree(routes, tree):
    for k, v in routes.items():
        if len(v) == 1:
            return [v]
        item = k
        parent = v[-1]
        childrens = v[:-1]
        tree.append([childrens, [item]])

    return tree


def transform(tree, new_node):
    print(tree)
    routes = {}
    build_routes(tree, routes)
    tree = []
    build_tree(routes, tree)
    print(routes)
    print(tree)


tree = ['A', [
            ['B', [
                ['D'],
            ]],
            ['C', [
                ['E'],
                ['F'],
            ]],
]]

# ['B', [
#     ['D'],
#     ['A', [
#         ['C', [
#             ['E'],
#             ['F'],
#         ]],
#     ]],
# ]]

print(transform(tree, 'a'))

#   B
#  / \
# D   A
#      \
#       C
#      / \
#     E   F

#     A
#    / \
#   B   C
#  /   / \
# D   E   F
