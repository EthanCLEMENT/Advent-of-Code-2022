with open('day3.txt', 'r') as f:
    rucksacks = f.read().strip().split('\n')

priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0

for i in rucksacks:
    mid = len(i) // 2
    compartment1, compartment2 = set(i[:mid]), set(i[mid:])
    common_prio = list(compartment1.intersection(compartment2))[0]
    ans += priorities.index(common_prio) + 1

print(f'Part 1: {ans}')

def score(char):
    return ord(char) - 38 - 58 * char.islower()

def part2(lines):
    for line in map(str.strip, lines):
        common = set(line) & set(next(lines)) & set(next(lines))
        yield score(common.pop())
print(sum(part2(open("day3.txt"))))

