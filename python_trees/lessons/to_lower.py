from hexlet.fs import mkdir, mkfile, is_directory, get_name, get_children, get_meta
from copy import deepcopy
from pprint import pprint

tree = mkdir('QwE', [
    mkfile('oNe'),
    mkfile('Two'),
    mkdir('THREE'),
])


# Приведение к нижнему регистру имен директорий и файлов внутри конкретной
# директории
def to_lower(node):
    if is_directory(node):
        return mkdir(get_name(node).lower(), get_children(node), get_meta(node))
    return mkfile(get_name(node).lower(), get_meta(node))


childrens = deepcopy(get_children(tree))
new_childrens = (list(map(lambda x: to_lower(x), childrens)))
pprint(mkdir(get_name(tree).lower(), new_childrens, deepcopy(get_meta(tree))))
pprint(tree)
