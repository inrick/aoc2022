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
h, w = len(chart), len(chart[0])

def valid(a, b):  # valid to move from a to b
    if not (0 <= b[0] < h) or not (0 <= b[1] < w):
        return False
    ha, hb = chart[a[0]][a[1]], chart[b[0]][b[1]]
    return (hb - ha) == 1 or hb <= ha

def bfs(S, E):
    path = {}
    seen = set()
    q = [(None, S)]
    while q:
        prev, node = q.pop(0)
        path[node] = prev
        if node == E:
            break
        for i, j in (0,1), (1,0), (0,-1), (-1,0):
            target = (node[0]+i, node[1]+j)
            if target not in seen and valid(node, target):
                q.append((node, target))
                seen.add(target)
    if node != E:
        return -1
    steps = 0
    while node != S:
        node = path[node]
        steps += 1
    return steps

lens = []
for i, row in enumerate(chart):
    for j, lev in enumerate(row):
        if lev == 0 and (steps := bfs((i, j), E)) != -1:
            lens.append(steps)

print('a) %d' % bfs(S, E))
print('b) %d' % min(lens))
