m = [list(map(int, x.rstrip())) for x in open('input', 'r')]
w, h = len(m[0]), len(m)
assert w == h

vis = set()
for i in range(1, w-1):
    acc = m[0][i]
    for row in range(1, h-1):
        if acc < m[row][i]:
            vis.add((row,i))
        acc = max(acc, m[row][i])
    acc = m[h-1][i]
    for row in range(h-2, 0, -1):
        if acc < m[row][i]:
            vis.add((row,i))
        acc = max(acc, m[row][i])

for i in range(1, h-1):
    acc = m[i][0]
    for col in range(1, w-1):
        if acc < m[i][col]:
            vis.add((i,col))
        acc = max(acc, m[i][col])
    acc = m[i][h-1]
    for col in range(w-2, 0, -1):
        if acc < m[i][col]:
            vis.add((i,col))
        acc = max(acc, m[i][col])

print('a) %d' % (4*w - 4 + len(vis)))

scenic = [[0]*w for _ in range(h)]
for ri in range(h):
    for cj in range(w):
        height = m[ri][cj]
        up = 0
        for row in range(ri-1, -1, -1):
            up += 1
            if m[row][cj] >= height:
                break
        down = 0
        for row in range(ri+1, h):
            down += 1
            if m[row][cj] >= height:
                break
        left = 0
        for col in range(cj-1, -1, -1):
            left += 1
            if m[ri][col] >= height:
                break
        right = 0
        for col in range(cj+1, w):
            right += 1
            if m[ri][col] >= height:
                break
        scenic[ri][cj] = up*down*left*right

print('b) %d' % max(map(max, scenic)))
