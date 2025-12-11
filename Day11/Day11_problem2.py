import re
from collections import defaultdict


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

memo = {}
def count_paths(node, end, has_fft, has_dac):
    # Check if we already computed this
    memo_key = (node.name, has_fft, has_dac)
    if memo_key in memo:
        return memo[memo_key]
    # Update flags if we're at a required node
    if node.name == 'fft':
        has_fft = True
    if node.name == 'dac':
        has_dac = True
    # Path found
    if node == end:
        # Void paths without both flags
        result = 1 if has_fft and has_dac else 0
        # Update memo
        memo[memo_key] = result
        return result
    # Dead end
    if not node.connections:
        # Update memo
        memo[memo_key] = 0
        return 0
    # Sum paths
    count = 0
    for neighbor in node.connections:
        count += count_paths(neighbor, end, has_fft, has_dac)
    memo[memo_key] = count
    return count


if __name__ == "__main__":
    nodes = defaultdict(list)
    for line in open("input.txt").readlines():
        parts = re.findall(r"\w+", line)
        if parts:
            idx = parts[0]

            if idx not in nodes:
                nodes[idx] = Node(idx)

            connections = []
            for part in parts[1:]:
                if part not in nodes:
                    nodes[part] = Node(part)
                connections.append(nodes[part])

            nodes[idx].connections = connections

    print(count_paths(nodes["svr"], nodes["out"], False, False))
