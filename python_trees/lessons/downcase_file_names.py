# Реализуйте функцию downcase_file_names(), которая принимает на вход
# директорию (объект-дерево), приводит имена всех файлов в этой и во всех
# вложенных директориях к нижнему регистру. Результат в виде обработанной
# директории возвращается наружу:


from hexlet.fs import mkdir, mkfile, get_children, get_name, is_file, get_meta
import copy


def downcase_file_names(node):
    new_node = copy.deepcopy(node)
    name = get_name(new_node)
    meta = get_meta(new_node)
    if is_file(new_node):
        return mkfile(name.lower(), meta)
    childrens = get_children(new_node)
    new_childrens = list(map(downcase_file_names, childrens))
    return mkdir(name, new_childrens, meta)


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('hOsts'),
])

expected = {
        'name': '/',
        'meta': {},
        'type': 'directory',
        'children': [
            {
                'name': 'eTc',
                'meta': {},
                'type': 'directory',
                'children': [
                    {
                        'name': 'NgiNx',
                        'meta': {'size': 4000},
                        'type': 'directory',
                        'children': [],
                    },
                    {
                        'name': 'CONSUL',
                        'meta': {},
                        'type': 'directory',
                        'children': [
                            {
                                'name': 'config.json',
                                'type': 'file',
                                'meta': {'uid': 0},
                            },
                        ],
                    },
                ],
            },
            {'name': 'hosts', 'type': 'file', 'meta': {}},
        ],
    }


assert downcase_file_names(tree) == expected

