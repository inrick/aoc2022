from pathlib import Path

input = [x.rstrip() for x in open('input', 'r')]

tree = {}
i = 0
cur = None
root = Path('/')
while i < len(input):
    line = input[i]
    assert line[0] == '$'
    i += 1
    cmd = line[2:]
    if cmd[:2] == 'cd':
        path = cmd[3:]
        cur = root if path == '/' else (cur / path).resolve()
    else:
        assert cmd == 'ls'
        while i < len(input) and (line := input[i])[0] != '$':
            c = line.split()
            if c[0] != 'dir':
                c[0] = int(c[0])
            if cur not in tree:
                tree[cur] = []
            tree[cur].append(c)
            i += 1

size = {}
def fillsize(p):
    n = 0
    for it in tree[p]:
        if it[0] == 'dir':
            n += fillsize(p / it[1])
        else:
            n += it[0]
    size[p] = n
    return n
fillsize(root)

target = root
for d, s in size.items():
    if s > size[root] - 40_000_000 and size[d] < size[target]:
        target = d

print('a) %d' % sum(s for s in size.values() if s < 100_000))
print('b) %d' % size[target])
