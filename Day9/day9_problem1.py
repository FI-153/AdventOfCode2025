def compute_area(x1, y1, x2, y2) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def get_points(filename="input.txt"):
    with open(filename, "r") as f:
        points_str = f.read().strip().split("\n")
    
    points = []
    for p_str in points_str:
        if p_str:
            x, y = map(int, p_str.split(","))
            points.append((int(x), int(y)))
    return points

def find_max_area(points):
    max_area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            max_area = max(compute_area(x1, y1, x2, y2), max_area)
    return max_area

if __name__ == "__main__":
    points = get_points()
    result = find_max_area(points)
    print(result)