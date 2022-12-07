from collections import deque

def all_unique(seq):
    for i, elem in enumerate(seq):
        try:
            seq.index(elem, 0, i)
        except ValueError:
            continue
        return False
    else:
        return True

def part_1(data, window=4):
    buffer = deque((), maxlen=window)
    for i, char in enumerate(data):
        if all_unique(buffer) and len(buffer) == window:
            return i
        else:
            buffer.append(char)

def part_2(data, window=14):
    return part_1(data, window)
