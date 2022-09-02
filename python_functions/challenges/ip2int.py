# Реализуйте и экспортируйте функции ip2int и int2ip, которые преобразовывают
# представление IP-адреса из десятичного формата с точками в 32-битное число в
# десятичной форме и обратно.

# Функция ip2int принимает на вход строку и должна возвращать число. А функция
# int2ip наоборот: принимает на вход число, а возвращает строку.


def ip2int(ip: str) -> int:
    ip_list = list(map(int, ip.split('.')))
    result = (
        (16777216 * ip_list[0]) +
        (65536 * ip_list[1]) +
        (256 * ip_list[2]) +
        ip_list[3])
    return result


def int2ip(nums: int) -> str:
    nums_list = (
        [int(nums / 16777216) % 256] +
        [int(nums / 65536) % 256] +
        [int(nums / 256) % 256] +
        [int(nums) % 256])
    return '.'.join(map(str, nums_list))


assert ip2int('128.32.10.1') == 2149583361
assert ip2int('0.0.0.0') == 0
assert ip2int('255.255.255.255') == 4294967295

assert (int2ip(2149583361)) == '128.32.10.1'
assert int2ip(0) == '0.0.0.0'
assert int2ip(4294967295) == '255.255.255.255'
