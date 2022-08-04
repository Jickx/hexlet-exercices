# triple = ('A', 'B', 'C')
# rotate_left(triple)  => ('B', 'C', 'A')
# rotate_right(triple)  => ('C', 'A', 'B')

def rotate_left(triple):
    return (triple[1], triple[2], triple[0])

def rotate_right(triple):
    return (triple[2], triple[0], triple[1])

print(rotate_left(('A', 'B', 'C')))