from functools import cmp_to_key

input = open('input', 'r').read().rstrip().split('\n\n')
input = [tuple(map(eval, x.split('\n'))) for x in input]

def inorder(a, b):
    for l, r in zip(a, b):
        if type(l) == int and type(r) == int:
            if l == r:
                continue
            elif l < r:
                return 1
            else:
                return -1
        else:
            if type(l) == int:
                l = [l]
            if type(r) == int:
                r = [r]
            c = inorder(l, r)
            if c == 0:
                continue
            return c
    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        return 0

ordered = [i+1 for i, (a, b) in enumerate(input) if inorder(a, b) == 1]

pp = [x for xx in input for x in xx] + [[[2]], [[6]]]
pp.sort(key=cmp_to_key(inorder), reverse=True)
key = (pp.index([[2]])+1) * (pp.index([[6]])+1)

print('a) %d' % sum(ordered))
print('b) %d' % key)
