input = open('input', 'r').read().rstrip()

def solve(n):
    return next(i+n for i in range(len(input)) if len(set(input[i:i+n])) == n)

print('a) %d' % solve(4))
print('b) %d' % solve(14))
