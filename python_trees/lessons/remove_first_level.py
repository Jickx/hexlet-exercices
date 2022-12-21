# Реализуйте функцию remove_first_level(), которая принимает на вход дерево и
# возвращает новое, элементами которого являются дети вложенных узлов.


def remove_first_level(tree: list) -> list:
    lst = []
    child_list = [x for x in tree if isinstance(x, list)]
    for x in child_list:
        lst.extend(x)
    return lst


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))  # [3, 5, [4, 3], 2]
