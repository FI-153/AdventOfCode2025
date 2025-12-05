def num_rolls():

    has_roll = []
    moves = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    num_moved = 0
    with open("input.txt") as f:
        for line in f:
            row = [False for _ in range(len(line.strip()))]
            for i in range(len(line.strip())):
                row[i] = True if line.strip()[i] == '@' else False

            has_roll.append(row)

    for i in range(len(has_roll[0])):
        for j in range(len(has_roll)):

            if not has_roll[i][j]: continue

            adjecents = 0

            #[i][j] -> Explore around [i][j]
            for move in moves:
                ii, jj = i+move[0], j+move[1]
                if ii >= 0 and ii < len(has_roll[0]) and jj >= 0 and jj < len(has_roll) and has_roll[ii][jj]:
                    adjecents += 1
                if adjecents >= 4:
                    break

            #Exploration over -> determine if [i][j] can be moved
            if adjecents < 4:
                num_moved += 1

    print(num_moved)

if __name__ == "__main__":
    num_rolls()