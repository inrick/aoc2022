import re

pat = re.compile(r'\d+,\d+')
input = [pat.findall(x.rstrip()) for x in open('input', 'r')]
input = [[tuple(map(int, x.split(','))) for x in xx] for xx in input]

def orange(p, q):
    return range(p, q+1) if p < q else range(q, p+1)

def path(a, b):
    if a[0] == b[0]:
        return [(a[0], y) for y in orange(a[1], b[1])]
    else:
        assert a[1] == b[1]
        return [(x, a[1]) for x in orange(a[0], b[0])]

class Chart:
    def __init__(self, x0, x1, y0, y1, pp, floor=False):
        self.x0, self.x1 = x0, x1
        self.y0, self.y1 = y0, y1
        w, h = x1 - x0 + 1, y1 - y0 + 1
        self.chart = [['.']*w for _ in range(h)]
        for x, y in pp:
            self.chart[y-y0][x-x0] = '#'
        self.chart[0][500-x0] = '+'
        if floor:
            for x in range(w):
                self.chart[y1-y0][x] = '#'

    def canmove(self, x, y):
        x0, x1, y0, y1 = self.x0, self.x1, self.y0, self.y1
        if not (x0 <= x <= x1 and y0 <= y <= y1):
            return 0
        return 1 if self.chart[y-y0][x-x0] == '.' else -1

    def draw(self):
        print('\n'.join(''.join(x) for x in self.chart))

    def sand(self):
        return [x for xx in self.chart for x in xx].count('o')

    def sim(self):
        x0, y0 = self.x0, self.y0
        while True:
            outside = False
            s = [500, 0]
            n = 0
            while not outside:
                for dir in (0, 1), (-1, 1), (1, 1):
                    c = self.canmove(s[0]+dir[0], s[1]+dir[1])
                    if c == 0:
                        outside = True
                        break
                    elif c == 1:
                        s[0] += dir[0]
                        s[1] += dir[1]
                        break
                else:
                    if s != [500, 0]:
                        n += 1
                    self.chart[s[1]-y0][s[0]-x0] = 'o'
                    break
            if n == 0:
                break
        return self

pp = [path(a, b) for p in input for a, b in zip(p, p[1:])]
pp = [x for xx in pp for x in xx]
x0, x1 = min(x for x, _ in pp), max(x for x, _ in pp)
y0, y1 = 0,                     max(y for _, y in pp)

print('a) %d' % Chart(x0, x1, y0, y1, pp).sim().sand())
# Add some silly amount of floor space. Should really do this in a nicer way.
print('b) %d' % Chart(x0-500, x1+500, y0, y1+2, pp, floor=True).sim().sand())
