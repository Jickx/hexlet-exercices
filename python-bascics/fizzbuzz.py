# fizz_buzz(1, 5) => 1 2 Fizz 4 Buzz
# fizz_buzz(11, 20) => 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

def fizz_buzz(begin, end):
    result = ''
    if begin > end:
        return result
    for i in range(begin, end + 1):
        if result:
            result += ' '
        if i % 5 == 0 and i % 3 == 0:
            result += 'FizzBuzz'
        elif i % 5 == 0:
            result += 'Buzz'
        elif i % 3 == 0:
            result += 'Fizz'
        else:
            result += f'{i}'
    return result

assert fizz_buzz(1, 5) == '1 2 Fizz 4 Buzz'
assert fizz_buzz(11, 20) == '11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz'

