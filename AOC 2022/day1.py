with open("day1.txt", 'r') as f:
    calories = [line.split(',') for line in f.read().splitlines()]

curr = 0
highest = 0
top3 = []

for i in range(len(calories)):
    print(curr, highest, calories[i])
    if calories[i][0] == '':
        if curr > highest:
            highest = curr
            top3.append(highest)
            curr = 0
        else:
            curr = 0
    else:
        curr += int(calories[i][0])

print(highest) #part 1
print(sum(top3[-3:])) #part 2



