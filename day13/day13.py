import numpy as np

file_path = './day13/day13.txt'
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]

# lines = [
# "#.##..##.", 
# "..#.##.#.", 
# "##......#", 
# "##......#", 
# "..#.##.#.", 
# "..##..##.", 
# "#.#.##.#.", 
# '',
# "#...##..#", 
# "#....#..#", 
# "..##..###", 
# "#####.##.", 
# "#####.##.", 
# "..##..###", 
# "#....#..#", 
# ]


patterns = []
curr = []
for l in lines:
    if l == '':
        patterns.append(curr)
        curr = []
    else:
        curr.append(l)
if curr:
    patterns.append(curr)


def find_right_borders(pattern):
    res = []
    prev_line = pattern[0]
    for i, line in enumerate(pattern[1:], 1):
        if (line == prev_line).all():
            res.append(i)
        prev_line = line
    return res

def count_reflected(pattern, right_border):
    if not right_border:
        return 0
    
    res = right_border

    left_border = right_border - 1
    while (left_border > 0) and (right_border < len(pattern) - 1):
        right_border += 1
        left_border -= 1
        if (pattern[right_border] != pattern[left_border]).any():
            return 0

    return res

def process_pattern(pattern):
    right_borders = find_right_borders(pattern)
    if right_borders:
        for right_border in right_borders:
            reflections = count_reflected(pattern, right_border)
            if reflections:
                return reflections
        return reflections
    else:
        return 0

total = 0
for pattern in patterns:
    pattern = np.array([list(line) for line in pattern])
    horizontal = process_pattern(pattern)
    vertical = process_pattern(pattern.T)
    res = 100*horizontal + vertical
    total += res   

print(total)
