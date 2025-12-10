import re
import itertools

# Translate the expected state and the buttons to their representation in base 2 then brute-force all combinations
# Starting from the smallest ones untill all the lights have been triggered correctly

def solve_machine(line):

    # Extract Target Diagram [...]
    diagram_match = re.search(r'\[([\.#]+)\]', line)
    if not diagram_match: return 0
    diagram_str = diagram_match.group(1)

    # Convert diagram to binary vector
    # . = 0, # = 1
    target_vector = 0
    for i, char in enumerate(diagram_str):
        if char == '#':
            target_vector = target_vector | (1 << i)

    # Extract Button Schematics (...)
    button_matches = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for b_str in button_matches:
        b_vector = 0
        indices = [int(x) for x in b_str.split(',')]
        for idx in indices:
            b_vector = b_vector | (1 << idx)
        buttons.append(b_vector)

    # Find minimum presses (Brute Force / BFS equivalent)
    # Check subsets of size 1 to N (start from the shortest combination)
    for r in range(len(buttons) + 1):
        for subset in itertools.combinations(buttons, r):
            # XOR all buttons in this subset
            current_state = 0
            for b in subset:
                current_state = current_state ^ b

            if current_state == target_vector:
                # Leave as soon as we find the smallest combination that triggers all the lights
                return r

    return 0

lines = open("input.txt").read().strip().split("\n")

total_presses = 0
for line in lines:
    min_presses = solve_machine(line)
    total_presses += min_presses

print(f"Total Minimum Presses: {total_presses}")