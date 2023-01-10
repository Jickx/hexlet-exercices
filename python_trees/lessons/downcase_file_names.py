# Реализуйте функцию downcase_file_names(), которая принимает на вход
# директорию (объект-дерево), приводит имена всех файлов в этой и во всех
# вложенных директориях к нижнему регистру. Результат в виде обработанной
# директории возвращается наружу:


import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile, is_directory
from pprint import pprint


def downcase_file_names(node):
    new_meta = copy.deepcopy(get_meta(node))
    name = get_name(node)
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = map(downcase_file_names, children)
    return mkdir(name, list(new_children), new_meta)


from hexlet import fs


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])


# В реализации используем рекурсивный процесс,
# чтобы добраться до самого дна дерева.
def get_nodes_count(node):
    if fs.is_file(node):
        # Возвращаем 1 для учета текущего файла
        return 1
    # Если узел — директория, получаем его детей
    children = fs.get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого из детей,
    # вызывая рекурсивно нашу функцию get_nodes_count
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    return 1 + sum(descendant_counts)


print(get_nodes_count(tree))
