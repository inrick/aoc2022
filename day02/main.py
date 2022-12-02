c = ['Rock', 'Paper', 'Scissors']

# does a beat b
def beats(a, b):  return (c.index(a)-1)%3 == c.index(b)
def toolscore(a): return c.index(a) + 1
def howtowin(o):  return c[(c.index(o)+1)%3]
def howtolose(o): return c[(c.index(o)-1)%3]

def roundscore(them, me):
    if beats(them, me):
        return 0
    elif them == me:
        return 3
    else:
        return 6

with open('input', 'r') as f:
    input = []
    for m in f:
        input.append(m.rstrip().split(' '))

total = 0
for a, b in input:
    ta, tb = c[ord(a) - ord('A')], c[ord(b) - ord('X')]
    total += roundscore(ta, tb) + toolscore(tb)

print('a) %d' % total)

total = 0
for a, b in input:
    ta = c[ord(a) - ord('A')]
    if b == 'X':
        tb = howtolose(ta)
    elif b == 'Y':
        tb = ta
    else:
        tb = howtowin(ta)
    total += roundscore(ta, tb) + toolscore(tb)

print('b) %d' % total)
