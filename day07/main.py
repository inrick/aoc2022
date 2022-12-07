from pathlib import Path

input = [x.rstrip() for x in open('input', 'r')]
tree = {}
i, cur = 0, Path()
while i < len(input):
    line = input[i]
    assert line[0] == '$'
    i += 1
    cmd = line[2:]
    if cmd[:2] == 'cd':
        path = cmd[3:]
        cur = (cur / path).resolve()
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

root = Path('/')
size = {}
def calc(p):
    size[p] = sum(calc(p / file) if t == 'dir' else t for t, file in tree[p])
    return size[p]
calc(root)

target = root
for d, s in size.items():
    # to get enough space, need size[root] - s < 40_000_000
    if size[root] - 40_000_000 < s < size[target]:
        target = d

print('a) %d' % sum(s for s in size.values() if s < 100_000))
print('b) %d' % size[target])
