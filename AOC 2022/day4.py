with open('day4.txt') as f:
    lines = f.read().splitlines()

couples = [tuple(tuple(map(int, elf.split('-'))) for elf in line.split(',')) for line in lines]
pair_count = 0
partial_count = 0
for couple in couples:
    elf1, elf2 = couple
    elf1_l, elf1_r = elf1
    elf2_l, elf2_r = elf2
    if elf1_l < elf2_l:
        if elf1_r >= elf2_r:
            pair_count += 1
            partial_count += 1
            
        elif elf1_r >= elf2_l:
            partial_count += 1
            
        else:
            continue
    elif elf2_l < elf1_l:
        if elf2_r >= elf1_r:
            pair_count += 1
            partial_count += 1
            
        elif elf2_r >= elf1_l:
            partial_count += 1
            
        else:
            continue
    else:
        pair_count += 1
        partial_count += 1
        
print(pair_count)
print(partial_count)
