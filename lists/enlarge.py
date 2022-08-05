# Реализуйте функцию enlarge(), которая принимает изображение в виде
# двумерного списка строк и увеличивает его в два раза, то есть удваивает
# каждый символ по горизонтали и вертикали.


def enlarge(image):
    result = []
    for line in image:
        result_line = ''
        for el in line:
            result_line += el * 2
        result.extend([
            result_line,
            result_line])
    return result


def show(image):
    for line in image:
        print(line)


dot = ['@']
show(enlarge(dot))
# => @@
# => @@
frame = [
    '****',
    '*  *',
    '*  *',
    '****'
]
show(frame)
# => ****
# => *  *
# => *  *
# => ****
show(enlarge(frame))
# => ********
# => ********
# => **    **
# => **    **
# => **    **
# => **    **
# => ********
# => ********
