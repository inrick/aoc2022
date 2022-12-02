# golfier solution than first, let (rock, paper, scissors) = (0, 1, 2)
input = [x.rstrip().split(' ') for x in open('input', 'r')]
input = [(ord(x) - ord('A'), ord(y) - ord('X')) for x, y in input]

ta, tb = 0, 0
for a, b in input:
    ta += 3*(a == b) + 6*((a+1)%3 == b) + b + 1
    b = [(a-1)%3, a, (a+1)%3][b]
    tb += 3*(a == b) + 6*((a+1)%3 == b) + b + 1

print('a) %d' % ta)
print('b) %d' % tb)
