import math


# Reusing the DSU class from Part 1
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True  # Merge occurred
        return False


def solve_part2():
    points = []
    lines = open("input.txt").readlines()

    for line in lines:
        line = line.strip()
        parts = line.split(',')
        if len(parts) == 3:
            points.append(tuple(map(int, parts)))

    n = len(points)

    # Compute and Sort Edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])

    # Kruskal's until fully connected
    dsu = DSU(n)
    num_components = n

    for _, u, v in edges:
        # If union returns True, a merge happened
        if dsu.union(u, v):
            num_components -= 1

            # If we just hit 1 component, this is the last necessary edge
            if num_components == 1:
                x1 = points[u][0]
                x2 = points[v][0]
                print(f"Final Connection: {points[u]} <-> {points[v]}")
                print(f"Product of X: {x1} * {x2} = {x1 * x2}")
                return


if __name__ == "__main__":
    solve_part2()