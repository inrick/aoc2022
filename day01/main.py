elves = []
with open('input', 'r') as f:
    elf = []
    for l in f:
        l = l.strip()
        if l == '':
            elves.append(elf)
            elf = []
        else:
            elf.append(int(l))
    if elf:
        elves.append(elf)

top = sorted(map(sum, elves), reverse=True)
print('a) %d' % top[0])
print('b) %d' % sum(top[:3]))
