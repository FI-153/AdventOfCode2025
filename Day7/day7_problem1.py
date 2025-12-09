def num_splits():

    def find_chars_idxs(line:str, c_to_find:str) -> set[int]:
        return set(i for i, c in enumerate(line) if c == c_to_find)

    lines = open("input.txt").readlines()

    rays = find_chars_idxs(lines[0], "S")

    num_splits = 0
    for line in lines[1:]:
        splitters = find_chars_idxs(line, "^")

        if len(splitters) == 0: continue

        #Find where the rays meet the splitters
        intersection = rays & splitters

        #Count the number of splits
        num_splits += len(intersection)

        #Determine the splitted rays positions
        splitted_rays = set([i+1 for i in intersection] + [i-1 for i in intersection])

        # Determine which rays are passing (Those that do not hit a splitter)
        passing_rays = rays - splitters - splitted_rays

        # Determine the new rays
        rays = splitted_rays | passing_rays

    print(num_splits)

if __name__ == "__main__":
    num_splits()