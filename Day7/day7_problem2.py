from collections import defaultdict

# Apply dynamic programming to tackle an otherwise combinatorial problem
def num_timelines():
    lines = open("input.txt").readlines()

    current_timelines = defaultdict(int)
    current_timelines[lines[0].find("S")] = 1

    for line in lines:
        if "^" not in line: continue

        next_timelines = defaultdict(int)

        for idx, n_timelines in current_timelines.items():
            if line[idx] == "^":
                # Split the timelines
                # Each new timeline carries along all the previous ones
                next_timelines[idx+1] += n_timelines
                next_timelines[idx-1] += n_timelines
            else:
                # Pass the timeline along
                next_timelines[idx] += n_timelines

        current_timelines = next_timelines

    print(sum(current_timelines.values()))

if __name__ == "__main__":
    num_timelines()