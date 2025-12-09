from collections import defaultdict

def num_timelines():
    lines = open("input.txt").readlines()

    # Initialize state: {column_index: number_of_timelines}
    # We start with 1 timeline at the 'S' position.
    start_index = lines[0].find("S")
    current_timelines = defaultdict(int)
    current_timelines[start_index] = 1

    for line in lines[1:]:

        if '^' not in line: continue

        next_timelines = defaultdict(int)

        # Iterate through every position where we currently have active beams
        for col_idx, count in current_timelines.items():

            if line[col_idx] == '^':
                # SPLIT: The count duplicates to both left and right timelines
                # If 50 timelines hit this splitter, 50 go left AND 50 go right.
                next_timelines[col_idx - 1] += count
                next_timelines[col_idx + 1] += count
            else:
                # PASS: The count continues straight down
                # If 50 timelines hit empty space, 50 continue to the same index.
                next_timelines[col_idx] += count

        # Move to the next row
        current_timelines = next_timelines

    # The result is the total number of timelines active at the very end
    print(f"Total timelines: {sum(current_timelines.values())}")

if __name__ == "__main__":
    num_timelines()