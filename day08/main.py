import numpy as np

m = np.array([list(map(int, x.rstrip())) for x in open('input', 'r')])
w, h = m.shape

vis = np.zeros((w-2, h-2), dtype=int)
for i in range(4):
    vis |= np.rot90((m[1:] > np.maximum.accumulate(m, axis=0)[:-1])[:-1,1:-1], k=4-i)
    m = np.rot90(m)

print('a) %d' % (4*(w-1)+np.sum(vis)))

def count(height, rows, cols):
    n = 0
    for row in rows:
        for col in cols:
            n += 1
            if m[row, col] >= height:
                return n
    return n

scenic = np.zeros((w, h), dtype=int)
for ri in range(1,h-1):
    for cj in range(1,w-1):
        up    = count(m[ri,cj], range(ri-1, -1, -1), [cj])
        down  = count(m[ri,cj], range(ri+1, h), [cj])
        left  = count(m[ri,cj], [ri], range(cj-1, -1, -1))
        right = count(m[ri,cj], [ri], range(cj+1, w))
        scenic[ri][cj] = up*down*left*right

print('b) %d' % np.max(scenic))
