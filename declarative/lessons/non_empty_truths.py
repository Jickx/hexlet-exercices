# Вам предстоит написать функцию non_empty_truths(), которая с помощью
# генераторов списков должна вычислять копию входного списка списков,
# "очищенную" от ложных элементов (не только False, а любых ложных!), а заодно
# и от пустых списков — таковые могу присутствовать сами по себе или могут
# получаться после отбрасывания из них всех элементов.


def non_empty_truths(list_of_lists: list[list]) -> list:
    return [
        truth for truth in [[
            elem for elem in one_list if elem
        ] for one_list in list_of_lists] if truth
    ]


print(non_empty_truths([]))  # нечего отбрасывать, это тоже нормально
# []
print(non_empty_truths([[], []]))  # пустые отбрасываем
# []
print(non_empty_truths([[0]]))  # чистим, чистые, но пустые тоже отбрасываем
# []
print(non_empty_truths([[0, ""], [False, None]]))  # в Python многое считается
# ложным
# []
print(non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]))
# [[1, 2], [True, 42]]
