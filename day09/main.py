import numpy as np

"""
width, height = 30, 30
ox, oy = 12, -5

def draw(kn):
    chart = [['.']*width for _ in range(height)]
    chart[height-1-kn[0][1]+oy][kn[0][0]+ox] = 'H'
    for i in range(1, len(kn)):
        chart[height-1-kn[i][1]+oy][kn[i][0]+ox] = '%d' % i
    for row in chart:
        print(''.join(row))
    print()
"""

steps = [x.rstrip().split() for x in open('input', 'r')]
steps = [(x, int(y)) for x, y in steps]

go = {
    'U': np.array([ 0, 1]),
    'D': np.array([ 0,-1]),
    'L': np.array([-1, 0]),
    'R': np.array([ 1, 0]),
}
diag = [
    np.array([ 1, 1]),
    np.array([ 1,-1]),
    np.array([-1,-1]),
    np.array([-1, 1]),
]

H, T = np.array([0,0]), np.array([0,0])

visited = set()
visited.add(tuple(T))
for dir, mag in steps:
    for _ in range(mag):
        H += go[dir]
        d = H-T
        for cmp in go.values():
            if np.array_equal(2*cmp, d):
                T += cmp
                break
            elif np.array_equal(cmp, d):
                break
        else:
            br = False
            for cmp in diag:
                for cmp2 in go.values():
                    if np.array_equal(H-(T+cmp), cmp2):
                        T += cmp
                        br = True
                        break
                if br: break
        visited.add(tuple(T))
        # draw(H, T)

print("a) %d" % len(visited))

kn = [np.array([0,0]) for _ in range(10)]

visited = set()
visited.add(tuple(kn[0]))
for dir, mag in steps:
    for _ in range(mag):
        kn[0] += go[dir]
        for i in range(1, len(kn)):
            d = kn[i-1] - kn[i]
            for cmp in go.values():
                if np.array_equal(2*cmp, d):
                    kn[i] += cmp
                    break
                elif np.array_equal(cmp, d):
                    break
            else:
                br = False
                for cmp in diag:
                    for cmp2 in go.values():
                        if np.array_equal(kn[i-1]-(kn[i]+cmp), cmp2):
                            kn[i] += cmp
                            br = True
                            break
                    if br: break
                else:
                    for cmp in diag:
                        if np.array_equal(2*cmp, d):
                            kn[i] += cmp
                            break
            if i == len(kn)-1:
                visited.add(tuple(kn[i]))
            # draw(kn)

print("b) %d" % len(visited))
