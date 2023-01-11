from hexlet import fs
from itertools import chain


def get_subdirectories_info(node):

    def count_files(node):
        if fs.is_file(node):
            return 1
        children = fs.get_children(node)
        count = list(map(count_files, children))
        return sum(count)

    def get_folders_info(node):
        childrens = fs.get_children(node)
        folders = list(filter(fs.is_directory, childrens))
        return list(map(
            lambda child: (fs.get_name(child), count_files(child)), folders
        ))

    return get_folders_info(node)


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
    ]),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
        fs.mkfile('file.tmp'),
        fs.mkdir('data'),
    ]),
    fs.mkfile('hosts'),
    fs.mkfile('resolve'),
])

assert get_subdirectories_info(tree) == [('etc', 1), ('consul', 2)]
