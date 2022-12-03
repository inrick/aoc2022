from functools import reduce

def prio(x): return ord(x) - (ord('a') - 1 if x.islower() else ord('A') - 27)

input = [x.rstrip() for x in open('input', 'r')]
ta = sum(prio((set(x[:len(x)//2]) & set(x[len(x)//2:])).pop()) for x in input)
tb = sum(
    prio(reduce(lambda x, y: x&y, map(set, input[i:i+3])).pop())
    for i in range(0, len(input), 3)
)

print('a) %d' % ta)
print('b) %d' % tb)
