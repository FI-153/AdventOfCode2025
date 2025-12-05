def num_rolls():

    def explore(i,j, rolls_to_remove):

        moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        adjecents = 0

        # [i][j] -> Explore around [i][j]
        for move in moves:
            ii, jj = i + move[0], j + move[1]
            if ii >= 0 and ii < len(has_roll[0]) and jj >= 0 and jj < len(has_roll) and has_roll[ii][jj] == 1:
                adjecents += 1
            if adjecents >= 4:
                break

        # Exploration over -> determine if [i][j] can be removed
        if adjecents < 4:
            rolls_to_remove.append((i,j))

    def build_matrix():
        has_roll = []
        with open("input.txt") as f:
            for line in f:
                row = [1 if c == "@" else 0 for c in line.strip()]
                has_roll.append(row)

        return has_roll

    has_roll = build_matrix()

    num_moved = 0

    while True:
        rolls_to_remove = []

        for i in range(len(has_roll[0])):
            for j in range(len(has_roll)):
                if has_roll[i][j] == 0: continue

                explore(i,j,rolls_to_remove)

        if len(rolls_to_remove) == 0: break

        for i, j in rolls_to_remove:
            has_roll[i][j] = 0
            num_moved += 1

    print(num_moved)

if __name__ == "__main__":
    num_rolls()