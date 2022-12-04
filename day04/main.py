import re
from itertools import starmap

pat = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)$')
input = [tuple(map(int, pat.findall(l)[0])) for l in open('input', 'r')]

def within (a0, a1, b0, b1): return (a0 <= b0 and b1 <= a1) or (b0 <= a0 and a1 <= b1)
def overlap(a0, a1, b0, b1): return (a0 <= b1 <= a1) or (b0 <= a1 <= b1)

print('a) %d' % sum(starmap(within, input)))
print('b) %d' % sum(starmap(overlap, input)))
