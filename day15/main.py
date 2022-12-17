import re

with open('input', 'r') as f:
    input = [list(map(int, re.findall(r'-?\d+', x))) for x in f]
    row = 2_000_000

def dist(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def rowcover(row):
    intervals = []
    for sx, sy, bx, by in input:
        d = dist((sx,sy), (bx,by))
        # Since we want abs(sx - x) <= d - abs(sy - row), there is not much use
        # trying to solve an impossible equation.
        if d - abs(sy - row) <= 0:
            continue
        x0 = sx - d + abs(sy - row)
        x1 = sx + d - abs(sy - row)
        intervals.append((x0, x1) if x0 < x1 else (x1, x0))
    intervals.sort()
    merged, m = [], None
    while intervals:
        x = intervals.pop(0)
        if m is None:
            m = x
        elif x[0] <= m[1]+1:
            m = [m[0], max(m[1], x[1])]
        else:
            merged.append(m)
            m = x
    if m:
        merged.append(m)
    return merged

def tuning(p): return 4_000_000*p[0]+p[1]

print('a) %d' % sum(x[1]-x[0] for x in rowcover(row)))

for row in range(4_000_001):
    if len(c := rowcover(row)) > 1:
        break
p = (c[0][1]+1, row)
print('b) %d' % tuning(p))
