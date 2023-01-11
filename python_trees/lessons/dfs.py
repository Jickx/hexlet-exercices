# Реализовать функцию, которая меняет владельца для всего дерева, то есть всех
# директорий и файлов.


from hexlet import fs
from copy import deepcopy
from pprint import pprint

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


def dfs(tree):
    print(fs.get_name(tree))
    if fs.is_file(tree):
        return
    children = fs.get_children(tree)
    list(map(dfs, children))


def change_owner(node, owner):
    name = fs.get_name(node)
    meta = fs.get_meta(deepcopy(node))
    meta['owner'] = owner
    if fs.is_file(node):
        return fs.mkfile(name, meta)
    childrens = fs.get_children(node)
    new_children = list(map(lambda child: change_owner(child, owner), childrens))
    return fs.mkdir(name, new_children, meta)


pprint(change_owner(tree, 'hexlet'))
