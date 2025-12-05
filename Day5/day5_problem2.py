import time

def count_fresh():
    fresh_ranges = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if "-" in line:
                fresh_ranges.append(
                    (
                        int(line.split("-")[0]),
                        int(line.split("-")[1])
                    )
                )
            else:
                break

    fresh_ranges.sort()

    num_fresh = 0

    #Set up the first range
    start, end = fresh_ranges[0]
    for i in range(1, len(fresh_ranges)):
        next_start, next_end = fresh_ranges[i]

        if end >= next_start:
            end = max(next_end, end)
        else:
            num_fresh += (end-start+1)
            start, end = next_start, next_end

    #Handle the last range which has already been set up
    num_fresh += (end-start+1)

    print(num_fresh)

start_time = time.time()
count_fresh()
print(f"Elapsed time: {time.time()-start_time:.4f} seconds")