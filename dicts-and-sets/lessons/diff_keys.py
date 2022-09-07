# В этом упражнении вам предстоит анализировать изменения, имея старую и новую
# версии словаря. Требуется реализовать функцию diff_keys(), которая должна
# принимать два словаря-аргумента — "старый" и "новый" — и возвращать словарь с
# результатами анализа. Результирующий словарь должен содержать строго три
# ниже перечисленных ключа:
# 'kept' — множество ключей, которые присутствовали в старом словаре и
# остались в новом;
# 'added' — множество ключей, которые отсутствовали в старом словаре, но
# появились в новом;
# 'removed' — множество ключей, которые присутствовали в старом словаре, но в
# новый не вошли.


def diff_keys(old: dict, new: dict) -> dict:
    output = {}
    old_set, new_set = set(old), set(new)
    output['kept'] = old_set & new_set
    output['added'] = new_set - old_set
    output['removed'] = old_set - new_set
    return output


old = {'x': 100, 'y': 200, 'z': 105}
new = {'x': 100, 'y': 200, 'velocity': 2.5}
diff = diff_keys(old, new)
assert isinstance(diff, dict)
assert set(diff.keys()) == {'added', 'removed', 'kept'}
assert diff['kept'] == {'x', 'y'}
assert diff['added'] == {'velocity'}
assert diff['removed'] == {'z'}
