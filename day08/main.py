import numpy as np

m = np.array([list(map(int, x.rstrip())) for x in open('input', 'r')])
w, h = m.shape

vis = np.zeros((w-2, h-2), dtype=int)
for i in range(4):
    vis |= np.rot90((m[1:] > np.maximum.accumulate(m, axis=0)[:-1])[:-1,1:-1], k=4-i)
    m = np.rot90(m)
print('a) %d' % (4*(w-1)+np.sum(vis)))

scenic = np.zeros((w, h), dtype=int)

for ri in range(1,h-1):
    for cj in range(1,w-1):
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

print('b) %d' % np.max(scenic))
