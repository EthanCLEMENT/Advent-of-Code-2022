
with open("day6.txt")as f:
    line = f.read()

print(next(i+4 for i in range(1,len(line))if len(set(line[i:i+4]))==4))

print(next(i+14 for i in range(1,len(line))if len(set(line[i:i+14]))==14))
