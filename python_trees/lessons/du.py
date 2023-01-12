# Реализуйте функцию du, которая принимает на вход директорию, а возвращает
# список узлов, вложенных (директорий и файлов) в указанную директорию на
# один уровень, и место, которое они занимают. Размер файла задается в
# метаданных. Размер директории складывается из сумм всех размеров файлов,
# находящихся внутри во всех подпапках.


from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def get_overall_files_size(node):
    childrens = get_children(node)
    if is_file(node):
        return get_meta(node)['size']
    folder_size = list(map(get_overall_files_size, childrens))
    return sum(folder_size)


def du(node):
    childrens = get_children(node)
    overall_sizes = list(map(
        lambda child: (get_name(child), get_overall_files_size(child)),
        childrens
    ))
    return sorted(overall_sizes, key=lambda size: size[1], reverse=True)



tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(du(tree))  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
