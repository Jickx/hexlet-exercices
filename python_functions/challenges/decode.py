# Реализуйте функцию decode(), которая принимает cтроку в виде графического
# представления линейного сигнала и возвращает строку с бинарным кодом.

def decode(signal: str) -> str:
    status = False
    result = ''
    for i in signal:
        if i == '|':
            status = True
            continue
        if status:
            result += '1'
            status = False
        else:
            result += '0'
            status = False
    return result


assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'
