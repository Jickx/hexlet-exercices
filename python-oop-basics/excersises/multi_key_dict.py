class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.

        """
        # BEGIN (write your solution here)
        self.data = {}
        self.alias_data = {}
        for k, v in kwargs.items():
            self.data[k] = v
        # END

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.

        """
        # BEGIN (write your solution here)
        if key in self.data:
            return self.data[key]
        return self.data[self.alias_data[key]]
        # END

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.

        """
        # BEGIN (write your solution here)
        if key in self.data:
            self.data[key] = value
        self.data[self.alias_data[key]] = value
        # END

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.

        """
        # BEGIN (write your solution here)
        for k, v in kwargs.items():
            self.alias_data[k] = v
        # END


mkd = MultiKeyDict(x=100, y=[10, 20])


print(mkd.__dict__)
mkd.alias(z='x')  # 'z' теперь означает то же, что и 'x'
print(mkd.__dict__)
print(mkd['z'])
# => 100
mkd['z'] += 1  # Можно даже менять значение через присваивание,
print(mkd['x'])       # что затронет и оригинальный ключ.
# => 101
mkd.alias(z='y')  # Теперь 'z' уже равнозначен 'y'
print(mkd.__dict__)
mkd['z'] += [30]
print(mkd['y'])
# => [10, 20, 30]
