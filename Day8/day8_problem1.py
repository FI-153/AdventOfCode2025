import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False


def solve():
    points = []
    lines = open("input.txt").readlines()

    for line in lines:
        line = line.strip()
        parts = line.split(',')
        if len(parts) == 3:
            points.append(tuple(map(int, parts)))

    # Compute pairwise distances
    # Store (distance, u, v).
    edges = []
    n = len(points)
    for i in range(n):
        p1 = points[i]
        for j in range(i + 1, n):
            p2 = points[j]
            dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
            edges.append((dist, i, j))

    # Sort edges by distance (ascending)
    edges.sort(key=lambda x: x[0])

    # Process exactly the top 1000 edges
    dsu = DSU(n)
    LIMIT = 1000

    # We iterate exactly LIMIT times, regardless of whether a Union happens or not.
    for k in range(min(LIMIT, len(edges))):
        _, u, v = edges[k]
        dsu.union(u, v)

    # Collect component sizes
    root_sizes = {}
    for i in range(n):
        root = dsu.find(i)
        if root not in root_sizes:
            root_sizes[root] = dsu.size[root]

    # Sort sizes descending
    sorted_sizes = sorted(root_sizes.values(), reverse=True)

    # Multiply the 3 largest sizes
    result = 1
    for item in sorted_sizes[:3]:
        result *= item

    print(f"Final Answer: {result}")


if __name__ == "__main__":
    solve()