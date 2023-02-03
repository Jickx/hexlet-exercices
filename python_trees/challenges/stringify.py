from itertools import chain


def stringify(value, replacer=" ", spaces_count=1):
    result = []
    new_spaces_count = spaces_count

    def walk(node, spaces_count):
        for k, v in node.items():
            if isinstance(v, dict):
                node = v
                result.append(f"{replacer * spaces_count}{k}: {{")
                walk(node, spaces_count + new_spaces_count)
                result.append(f'{replacer * spaces_count}}}')
            else:
                result.append(f"{replacer * spaces_count}{k}: {v}")
    if isinstance(value, dict):
        walk(value, new_spaces_count)
    else:
        result.append(str(value))
    if len(result) == 1:
        return ''.join(result)
    return '{\n' + '\n'.join(result) + '\n}'


# print(stringify('hello'))  # значение приведено к строке, но не имеет кавычек
# hello
# stringify(True)
# True
# stringify(5)
# 5

data = {"hello": "world", "is": True, "nested": {"count": 5}}
print(stringify(data))  # то же самое что stringify(data, ' ', 1)
# {
#   hello: world
#   is: True
#   nested: {
#    count: 5
#   }
# }

# символ, переданный вторым аргументом повторяется столько раз, сколько
# указано третьим аргументом
print(stringify(data, '|-', 2))

# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }

nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}

print(stringify(nested, ' ', 2))
