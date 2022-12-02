with open("day2.txt", "r") as f:
    moves = f.read().split("\n")

scores = {"A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}

newrule = { "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X"
        }
ans = 0
for i in moves:
    ans += scores[i]

print(ans)

ans2 = 0
for i in moves:
    ans2 += scores[newrule[i]]
print(ans2)
