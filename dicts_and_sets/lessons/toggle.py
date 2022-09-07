# В этой практике вы будете реализовывать функции для работы с множествами,
# как с наборами флагов.
# Флаги удобны для управления работой некоторого кода: если флаг поднят,
# значит какая-то возможность включена. В этом плане флаги похожи на галочки в
# формах и бланках — галочку тоже можно поставить или не поставить.
# В нашем случае флаги будут представлять собой элементы множества: если
# элемент в множестве присутствует, значит и флаг поднят. Вам же нужно будет
# реализовать две функции: toggle() и toggled().
# Функция toggle()
# Эта функция должна принимать флаг (один!) и множество в качестве аргументов.
# Если флаг уже присутствует в множестве, его нужно из множества убрать. Если
# же флаг отсутствует, то его нужно добавить. Таким образом функция будет
# переключать состояние флага. Множество нужно заменять "по месту", возвращать
# из функции ничего не нужно.
# Функция toggled()
# Эта функция работает похожим на toggle() образом, но вместо изменения
# исходного множества возвращает новое — с уже переключенным флагом.

def toggle(flag: str, flags: set) -> None:
    flags.add(flag) if flag not in flags else flags.remove(flag)


def toggled(flag: str, flags: set) -> set:
    flags = flags.copy()
    flags.add(flag) if flag not in flags else flags.remove(flag)
    return flags


READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
assert (READ_ONLY in flags) is True
toggle(READ_ONLY, flags)
assert (READ_ONLY in flags) is False


READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
assert (READ_ONLY in flags) is False
assert (READ_ONLY in new_flags) is True
