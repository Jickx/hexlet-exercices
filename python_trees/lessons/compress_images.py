# Реализуйте функцию compress_images(), которая принимает на вход директорию,
# находит внутри нее картинки и "сжимает" их. Под сжиманием понимается
# уменьшение свойства size в метаданных в два раза. Функция должна вернуть
# обновленную директорию со сжатыми картинками и всеми остальными данными,
# которые были внутри этой директории.

from hexlet.fs import mkdir, mkfile, get_children, get_meta, get_name
import copy
from pprint import pprint


def compress_images(tree):
    new_tree = copy.deepcopy(tree)
    new_childrens = get_children(new_tree)

    def change_size(node):
        meta = get_meta(node)
        size = meta.get('size')
        if get_name(node).endswith('.jpg') and size:
            meta['size'] //= 2
            return mkfile(get_name(node), meta)
        else:
            return node

    childrens_list = list(map(lambda x: change_size(x), new_childrens))
    return mkdir(get_name(new_tree), childrens_list, get_meta(new_tree))


tree = mkdir('my documents', [
            mkfile(
                'avatar.jpg',
                {'size': 100, 'attributes': {'hide': False, 'read_only': True}},
            ),
            mkdir('presentations'),
        ], {'owner': 'hexlet'})

new_tree = compress_images(tree)
new_file = get_children(new_tree)[0]
new_file_meta = get_meta(new_file)
new_file_meta['attributes']['hide'] = True
old_file = get_children(tree)[0]
assert not get_meta(old_file)['attributes']['hide']

new_tree_meta = get_meta(new_tree)
new_tree_meta['owner'] = 'user'

pprint(compress_images(tree) == tree)
pprint(tree)

