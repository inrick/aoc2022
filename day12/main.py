def height(c):
    c = c.replace('S', 'a').replace('E', 'z')
    return ord(c) - ord('a')

input = [x.rstrip() for x in open('input', 'r')]
S, E = None, None
for i, row in enumerate(input):
    if (j := row.find('S')) != -1:
        S = i, j
    if (j := row.find('E')) != -1:
        E = i, j
chart = [[height(x) for x in xx] for xx in input]
ht = lambda x: chart[x[0]][x[1]]
h, w = len(chart), len(chart[0])

def valid(a, b):  # valid to move from a to b
    for x in a, b:  # check both in case we're moving from b to a
        if not (0 <= x[0] < h) or not (0 <= x[1] < w):
            return False
    return ht(b) - ht(a) <= 1

def bfs(S, valid, found):
    path = {}
    seen = set()
    q = [(None, S)]
    while q:
        prev, node = q.pop(0)
        path[node] = prev
        if found(node):
            break
        for i, j in (0,1), (1,0), (0,-1), (-1,0):
            target = (node[0]+i, node[1]+j)
            if target not in seen and valid(node, target):
                q.append((node, target))
                seen.add(target)
    if not found(node):
        return -1
    steps = 0
    while node != S:
        node = path[node]
        steps += 1
    return steps

print('a) %d' % bfs(S, valid, lambda x: x == E))
print('b) %d' % bfs(E, lambda a, b: valid(b, a), lambda x: ht(x) == 0))
