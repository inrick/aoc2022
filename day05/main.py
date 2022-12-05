import re
from copy import deepcopy

input = [x.rstrip() for x in open('input', 'r')]
sep = input.index('')
ncrates = len(input[sep-1].split())
crates = [[] for _ in range(ncrates)]
for line in input[:sep-1]:
    for j in range(1, len(line), 4):
        if line[j] != ' ':
            crates[j//4].append(line[j])
for c in crates:
    c.reverse()

pat = re.compile(r'^move (\d+) from (\d+) to (\d+)$')
moves = [tuple(map(int, pat.findall(m)[0])) for m in input[sep+1:]]

ca, cb = deepcopy(crates), deepcopy(crates)
for n, a, b in moves:
    for _ in range(n):
        ca[b-1].append(ca[a-1].pop())
    cb[b-1] += cb[a-1][-n:]
    cb[a-1]  = cb[a-1][:-n]

print('a) %s' % ''.join([c[-1] for c in ca]))
print('b) %s' % ''.join([c[-1] for c in cb]))
