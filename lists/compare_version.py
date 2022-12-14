# Реализуйте функцию compare_version(), которая сравнивает переданные версии
# version1 и version2. Если version1 > version2, то функция должна вернуть 1,
# если version1 < version2, то -1, если же version1 = version2 — 0.
# Версия — это строка, в которой два числа (мажорная и минорные версии)
# разделены точкой, например: 12.11. Важно понимать, что версия — это не число
# с плавающей точкой, а несколько чисел не связанных между собой. Проверка на
# больше/меньше производится сравнением каждого числа независимо. Поэтому
# версия 0.12 больше версии 0.2.


def compare_version(ver1: str, ver2: str) -> int:
    if ver1 == ver2:
        return 0
    ver1 = [int(i) for i in ver1.split('.')]
    ver2 = [int(i) for i in ver2.split('.')]
    if ver1[0] > ver2[0] or ver1[0] == ver2[0] and ver1[1] > ver2[1]:
        return 1
    return -1


assert compare_version("0.2", "0.12") == -1
assert compare_version("0.2", "0.1") == 1
assert compare_version("4.2", "4.2") == 0
