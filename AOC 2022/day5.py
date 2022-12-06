import re
from copy import deepcopy
with open("day5.txt", "r") as file:
    s, c = file.read().strip("\n").split("\n\n")
stacks1 = [list(''.join(x).strip()) for x in list(zip(*s.split("\n")[:-1]))[1::4]]
stacks2 = deepcopy(stacks1)
commands = [list(map(int, re.findall(r'\d+', x))) for x in c.split('\n')]
temp_stack = []
for command in commands:
    for i in range(command[0]):
        stacks1[command[2] - 1].insert(0, stacks1[command[1] - 1].pop(0))
        temp_stack.append(stacks2[command[1] - 1].pop(0))
    stacks2[command[2] - 1] = temp_stack + stacks2[command[2] - 1]
    temp_stack = []
print(f"Part 1: {''.join([x[0] for x in stacks1])}")
print(f"Part 2: {''.join([x[0] for x in stacks2])}")
