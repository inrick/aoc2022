from copy import deepcopy
from math import prod
import re

input = [x.rstrip() for x in open('input', 'r').read().split('\n\n')]
pat = re.compile(r'\d+')
patop = re.compile(r'Operation: (.*)$')

def expr(x):
    e = patop.findall(x)[0].split()
    assert len(e) == 5 and e[0] == 'new' and e[1] == '=' and e[2] == 'old'
    op = e[3]
    rhs = int(e[4]) if e[4] != 'old' else e[4]
    return (e[2], op, rhs)

def exec(e, val):
    rhs = val if e[2] == 'old' else e[2]
    if e[1] == '+':
        return val + rhs
    elif e[1] == '*':
        return val * rhs
    else:
        assert False

def parse(s):
    findall = lambda x: list(map(int, pat.findall(x)))
    findone = lambda x: int(pat.findall(x)[0])
    m, it = [], s.split('\n')
    for fn in [findone, findall, expr, findone, findone, findone]:
        m.append(fn(it[0]))
        it = it[1:]
    assert len(it) == 0
    return m

monkeys = list(map(parse, input))

def run(rounds, calm):
    mm = deepcopy(monkeys)
    inspect = [0]*len(mm)
    for round in range(rounds):
        for m in mm:
            for it in m[1]:
                inspect[m[0]] += 1
                it = calm(exec(m[2], it))
                if (it % m[3]) == 0:
                    mm[m[4]][1].append(it)
                else:
                    mm[m[5]][1].append(it)
            m[1] = []
    return inspect

def score(inspect):
    return prod(sorted(inspect, reverse=True)[:2])

# Find divisor common to all tests to keep worry in check.
div = prod(m[3] for m in monkeys)

print('a) %d' % score(run(20,     lambda x: x // 3)))
print('b) %d' % score(run(10_000, lambda x: x % div)))
