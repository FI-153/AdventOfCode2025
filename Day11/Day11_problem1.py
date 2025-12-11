from collections import defaultdict, deque
import re

def count_paths():
    nodes = defaultdict(list)

    for line in open("input.txt").readlines():
        parts = re.findall(r"\w+", line)
        if parts:
            nodes[parts[0]] = parts[1:]

    stack = deque([["you", False]])

    num_paths = 0
    while stack:
        elem, visited = stack[-1]

        if elem == "out":
            stack.pop()
            num_paths += 1
            continue

        if visited:
            stack.pop()
        else:
            stack[-1][1] = True
            for neighbour in nodes[elem]:
                if [neighbour, True] not in stack:
                    stack.append([neighbour, False])

    print(num_paths)

if __name__ == "__main__":
    count_paths()