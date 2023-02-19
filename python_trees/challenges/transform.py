# Реализуйте функцию transform(), которая строит дерево относительно заданного
# корневого узла.
# Функция на вход принимает 2 аргумента:
# - исходное дерево
# - узел, от которого будет построено новое дерево.
# Функция должна возвращать новое дерево с сохранёнными связями между узлами,
# в котором переданный узел является корневым.


def build_tree_dict(subtree, parent=None, result_dict={}):
    if len(subtree) == 2 and not isinstance(subtree[0], list):
        [node, child] = subtree
        result_dict[node] = parent
        parent = node
        return build_tree_dict(child, parent)
    for item in subtree:
        if len(item) == 1:
            [node] = item
            result_dict[node] = parent
        else:
            build_tree_dict(item, parent)
    return result_dict

list_of_lists = []


def build_tree_list(tree):
    result = []
    keys_list = [k for k in tree]

    def walk(subtree):
        for value in subtree.values():
            if value in values_set:
                result.append([value, ])


    return


from itertools import count
def key_to_values(tree):
    RvsD = dict()
    for k, v in tree.items():
        RvsD.setdefault(v, []).append(k)
    return RvsD




def transform(tree, new_node):
    return build_tree_dict(tree)


tree = ['A', [
    ['B', [
        ['D'],
    ]],
    ['C', [
        ['E'],
        ['F'],
    ]],
]]

#     A
#    / \
#   B   C
#  /   / \
# D   E   F


print(transform(tree, 'B'))
print(tree)
print(key_to_values({'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'C'}))

# ['B', [                 #   B
#     ['D'],              #  / \
#     ['A', [             # D   A
#         ['C', [         #      \
#             ['E'],      #       C
#             ['F'],      #      / \
#         ]],             #     E   F
#     ]],
# ]]
