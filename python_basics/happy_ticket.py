# is_happy_ticket('123123') # True
# is_happy_ticket('341800') # True
 
# is_happy_ticket('42') # False
# is_happy_ticket('12345678') # False

def is_happy_ticket(number):    
    centre = len(number) // 2
    number = [int(i) for i in number]
    return sum(number[centre:]) == sum(number[:centre])

print(is_happy_ticket('341800'))