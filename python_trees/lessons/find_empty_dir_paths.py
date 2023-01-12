from hexlet import fs


# Найдем все пустые директории в нашей файловой системе.
def find_empty_dir_paths(tree):

    def walk(node, depth):
        childrens = fs.get_children(node)
        if fs.is_directory(node) and not childrens:
            return fs.get_name(node)
        if depth == 2:
            return []
        folders_list = list(map(
            lambda child: walk(child, depth + 1), childrens
        ))
        return fs.flatten(folders_list)

    return walk(tree, 0)


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

print(find_empty_dir_paths(tree))  #['apache', 'data', 'logs']
