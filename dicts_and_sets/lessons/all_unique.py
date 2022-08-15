# Вам предстоит реализовать функцию all_unique(), которая должна принимать
# итератор (в т.ч. и те, которые не перезапускаемые!) и возвращать True, если
# элементы в итераторе не повторяются (если элементов нет, то ничего не
# повторяется!).

def all_unique(items):
    items = list(items)
    return len(items) == len(set(items))


assert all_unique(iter([])), "Should work with iterators."
assert all_unique(iter([1])), (
    "Should handle non-restartable iterators too."
)
assert all_unique([])
assert all_unique("cat")
assert not all_unique("lol")
