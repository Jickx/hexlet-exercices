# Реализуйте функцию get_hidden_files_count(), которая считает количество
# скрытых файлов в директории и всех поддиректориях. Скрытым файлом в Linux
# системах считается файл, название которого начинается с точки:

from hexlet.fs import mkdir, mkfile, is_file, get_name, get_children


def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node) and name.startswith('.'):
        return 1
    childrens = get_children(node)
    count = list(map(get_hidden_files_count, childrens))
    return sum(count)



tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(get_hidden_files_count(tree))  # 3