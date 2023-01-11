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


def get_nodes_cout(node):
    if fs.is_file(node):
        return 1
    childrens = fs.get_children(node)
    count = list(map(get_nodes_cout, childrens))
    return sum(count) + 1


print(get_nodes_cout(tree))
