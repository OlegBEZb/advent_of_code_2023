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


def check_pattern(pattern, smudge=False):
    # in assumption that the simmetry touches the border and this simmetry is unique
    for i in range(1, len(pattern)):
        ln = min(i, len(pattern) - i)
        if smudge:
            if np.sum(pattern[i-ln:i] != pattern[i:i+ln][::-1]) == 1:
                return i
        else:
            if (pattern[i-ln:i] == pattern[i:i+ln][::-1]).all():
                return i
    return 0


total = 0
for pattern in patterns:
    pattern = np.array([list(line) for line in pattern])

    horizontal = check_pattern(pattern, smudge=True)
    vertical = check_pattern(pattern.T, smudge=True)

    res = 100*horizontal + vertical
    total += res   

print(total)