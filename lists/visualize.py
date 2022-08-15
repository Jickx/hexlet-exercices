# Реализуйте функцию visualize(), которая подсчитывает сколько монет каждого
# номинала есть в копилке и показывает результат в виде графика. Каждый
# столбец графика — стопка монет опредлённого номинала.

# Для простоты условимся, что монеты в копилке всегда есть, и их количество не
# ограничено, а номинал может быть любым.

# Функция принимает на вход список или кортеж с числами и возвращает график в
# виде строки. Необязательный аргумент bar_char определяет символ, с помощью
# которого рисуется график. Значение по умолчанию — знак рубля (₽).

from collections import Counter


def visualize(coins, bar_char='₽') -> str:
    coins_count = {k: v for k, v in sorted(Counter(coins).items())}
    output = []
    output_string = ''
    max_count = max(coins_count.values())
    for key, count in coins_count.items():
        output.append(
            [f'{(bar_char * 2):<2}'] * count
            + [f'{count:<2}']
            + ['  '] * (max_count - count)
        )
    output = reversed(list(zip(*output)))
    for line in output:
        output_string += (' '.join(str(i) for i in line)) + '\n'
    output_string += '-----------------\n'
    output_string += '1  2  3  5  10 20'
    return output_string


MONEY = (
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)


assert visualize(MONEY) == """
   6             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2  2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1] # noqa

assert visualize(MONEY, bar_char='$') == """
   6             
   $$          5 
4  $$          $$
$$ $$          $$
$$ $$ 2  2  2  $$
$$ $$ $$ $$ $$ $$
$$ $$ $$ $$ $$ $$
-----------------
1  2  3  5  10 20
"""[1:-1] # noqa
