# Вам дан класс Counter, реализующий счетчик с инкрементом и декрементом.
# Вам нужно реализовать класс-потомок LimitedCounter, который будет отличаться
# от Counter тем, что при инициализации будет принимать в качестве аргумента
# лимит — максимальное возможное значение счетчика.
# Требования к классу LimitedCounter:
# Класс должен максимально использовать методы предка, если таковые
# переопределяет
# Минимальное значение счетчика Counter — 0, должно оставаться таковым и для
# LimitedCounter

class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


class LimitedCounter(Counter):
    def __init__(self, limit):
        self.limit = limit
        self._value = 0
        super().__init__()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = min(max(new_value, 0), self.limit)


counter = LimitedCounter(limit=10)
counter.inc()
counter.inc(7)
print(counter.value)  # 8
counter.dec(10)
print(counter.value)  # 0
counter.inc(7)
counter.inc(7)
print(counter.value)  # 10
