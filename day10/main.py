input = [x.rstrip().split() for x in open('input', 'r')]
input = [[x[0], int(x[1])] if len(x) > 1 else x for x in input]

latency = {'noop': 1, 'addx': 2}
strength, crt, row = [], [], [' ']*40
X, cycles = 1, 0
for instr in input:
    for _ in range(latency[instr[0]]):
        for i in -1, 0, 1:
            if X+i == cycles%40:
                row[X+i] = '#'
        cycles += 1
        if (cycles - 20)%40 == 0:
            strength.append(X*cycles)
        elif cycles%40 == 0:
            crt.append(row)
            row = [' ']*40
    if instr[0] == 'addx':
        X += instr[1]

print('a) %d' % sum(strength))
print('b)')
print('\n'.join(''.join(x) for x in crt))
