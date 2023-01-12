from hexlet import fs
from pprint import pprint


# Найдем все пустые директории в нашей файловой системе.
def find_empty_dir_paths(node):
    childrens = fs.get_children(node)
    if fs.is_directory(node) and not childrens:
        return fs.get_name(node)
    folders_list = list(map(find_empty_dir_paths, childrens))
    return fs.flatten(folders_list)


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
        fs.mkdir('consul', [
            fs.mkfile('config.json'),
            fs.mkdir('data'),
        ]),
    ]),
    fs.mkdir('logs'),
    fs.mkfile('hosts'),
])

assert find_empty_dir_paths(tree) == ['apache', 'data', 'logs']
