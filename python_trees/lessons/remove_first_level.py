# Реализуйте функцию remove_first_level(), которая принимает на вход дерево и
# возвращает новое, элементами которого являются дети вложенных узлов.

from itertools import chain


def remove_first_level(tree: list) -> list:
    childrens = filter(lambda node: isinstance(node, list), tree)
    return list(chain(*childrens))


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]
