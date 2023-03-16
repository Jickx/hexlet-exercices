# Реализуйте класс Counter, представляющий собой счётчик, хранящий
# неотрицательное целочисленное значение и позволяющий это значение изменять:
# атрибут value должен хранить текущее значение счётчика (вначале равное нулю)
# метод inc() должен увеличивать текущее значение на delta единиц (на 1 по
# умолчанию)
# метод dec() должен уменьшать текущее значение на delta единиц (на 1 по
# умолчанию)


class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value -= delta


c = Counter()
c.inc()
c.inc()
c.inc(40)
print(c.value)  # 42
c.dec()
c.dec(30)
print(c.value)  # 11
c.dec(delta=100)
print(c.value)  # 0
