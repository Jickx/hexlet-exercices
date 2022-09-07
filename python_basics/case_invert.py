def invert_case(text):
    inverted_text = ''
    for i in text:
        if i == i.lower():
            inverted_text += i.upper()
        else:
            inverted_text += i.lower()
    return inverted_text

print(invert_case('Hello, World!'))


