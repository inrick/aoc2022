input = open('input', 'r').read().rstrip()

a, b = None, None
for i in range(len(input)):
    if a is None and len(set(input[i:i+4])) == 4:
        a = i+4
    if b is None and len(set(input[i:i+14])) == 14:
        b = i+14
    if a and b:
        break

print('a) %d' % a)
print('b) %d' % b)
