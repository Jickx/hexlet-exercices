# line1 = (0, 10), (100, 130)
# is_vertical(line1) False
# is_horizontal(line1) False
# is_degenerated(line1) False
# is_inclined(line1) True
# line2 = (42, 1), (42, 2)
# is_vertical(line2) True
# line3 = (100, 50), (200, 50)
# is_horizontal(line3) True

def is_degenerated(line):
    p1, p2 = line
    return p1 == p2

def is_vertical(line):
    p1, p2 = line
    return p1[0] == p2[0] and not is_degenerated(line)

def is_horizontal(line):
    p1, p2 = line
    return p1[1] == p2[1] and not is_degenerated(line)

def is_inclined(line):
    p1, p2 = line
    return (p1[0] != p2[0] and p1[1] != p2[1]) and not is_degenerated(line)


VERTICAL = (15, 5), (15, -5)
HORIZONTAL = (5, 15), (-5, 15)
DEGENERATED = (42, 100), (42, 100)
INCLINED = (0, 0), (1, 1)


assert is_vertical(VERTICAL)
assert not is_vertical(HORIZONTAL)
assert not is_vertical(DEGENERATED)
assert not is_vertical(INCLINED)
assert not is_horizontal(VERTICAL)
assert is_horizontal(HORIZONTAL)
assert not is_horizontal(DEGENERATED)
assert not is_horizontal(INCLINED)
assert not is_degenerated(VERTICAL)
assert not is_degenerated(HORIZONTAL)
assert is_degenerated(DEGENERATED)
assert not is_degenerated(INCLINED)
assert not is_inclined(VERTICAL)
assert not is_inclined(HORIZONTAL)
assert not is_inclined(DEGENERATED)
assert is_inclined(INCLINED)


