import numpy as np

steps = [x.rstrip().split() for x in open('input', 'r')]
steps = [(['U', 'D', 'L', 'R'].index(x), int(y)) for x, y in steps]

M = np.array([
    [ 0,  0, -1,  1,  1,  1, -1, -1],
    [ 1, -1,  0,  0,  1, -1, -1,  1],
])
N = np.array([
    [ 1,  2,  2,  1, -1, -2, -2, -1],
    [ 2,  1, -1, -2, -2, -1,  1,  2],
])

knots = np.zeros((10, 2), dtype=int)

va, vb = set(), set()
for dir, mag in steps:
    for _ in range(mag):
        knots[0] += M[:,dir]
        for i in range(1, 10):
            d = knots[i-1] - knots[i]
            if (d[:,None] == M).all(axis=0).any():
                continue  # Still close enough
            elif (d[:,None] == 2*M).all(axis=0).any():
                knots[i] += d // 2  # Move in same direction
            elif (found := (d[:,None] == N).all(axis=0)).any():
                # Pick the diagonal move that catches up
                j = (found.nonzero()[0][0] // 2)
                knots[i] += M[:,4+j]
        va.add(tuple(knots[1]))
        vb.add(tuple(knots[9]))

print("a) %d" % len(va))
print("b) %d" % len(vb))
