# Реализуйте функцию compress_images(), которая принимает на вход директорию,
# находит внутри нее картинки и "сжимает" их. Под сжиманием понимается
# уменьшение свойства size в метаданных в два раза. Функция должна вернуть
# обновленную директорию со сжатыми картинками и всеми остальными данными,
# которые были внутри этой директории.

import copy
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(tree):
    tree_copy = copy.deepcopy(tree)
    childrens = get_children(tree_copy)
    for children in childrens:
        if get_name(children)[-4:] == '.jpg' and \
                children['meta'].get('size', None):
            children['meta']['size'] /= 2
    return tree_copy


tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
        mkfile('photo.jpg')
    ],
    {'hide': False}
)
print(compress_images(tree))
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }
