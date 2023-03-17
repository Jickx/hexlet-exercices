# Вам предстоит снова реализовать класс Counter. Но на этот раз счётчик
# будет иммутабельным и всё ещё неотрицательным целочисленным. Методы inc()
# и dec() должны возвращать новый счётчик с изменённым в большую или
# соответственно меньшую сторону значением value (по умолчанию счётчик
# изменяется на единицу).


class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return self.inc(- delta)


c = Counter()
print(c.inc().inc(5).dec(2).value)  # 4

# Старый экземпляр не должен изменяться
d = c.inc(100)
print(d.dec().value)  # 99

forty_two = Counter(42)
print(forty_two.value)  # 42
