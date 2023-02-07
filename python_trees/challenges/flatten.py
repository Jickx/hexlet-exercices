# Реализуйте функцию flatten(), которая делает плоским вложенный список.


def flatten(tree):
    result = []

    def walk(tree):
        for subtree in tree:
            if isinstance(subtree, list):
                walk(subtree)
            else:
                result.append(subtree)
    walk(tree)
    return result





print(flatten([]))  # []
print(flatten([2, [3, 5], [[4, 3], 2]]))  # [2, 3, 5, 4, 3, 2]
