# Реализуйте функцию decode(), которая принимает cтроку в виде графического
# представления линейного сигнала и возвращает строку с бинарным кодом.

def decode(signal: str) -> str:
    levels = ''.join(filter(lambda x: x != '|', signal))
    levels_shifted = signal[:1] + levels
    result = ''.join(map(lambda x, y: '1' if x != y else '0',
                         levels_shifted,
                         levels))
    return result


assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'
