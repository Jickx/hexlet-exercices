
# Реализуйте функцию find_files_by_name(), которая принимает на вход файловое
# дерево и подстроку, а возвращает список файлов, имена которых содержат эту
# подстроку. Функция должна вернуть полные пути файлам:


from hexlet.fs import mkdir, mkfile, get_name, get_children, is_file, flatten
from pprint import pprint
import os


def find_files_by_name(node, substring):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node) and substring in name:
            return new_ancestry
        childrens = get_children(node)
        files_list = list(map(
            lambda child: walk(child, new_ancestry), childrens
        ))
        return flatten(files_list)
    return walk(node, '')


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
