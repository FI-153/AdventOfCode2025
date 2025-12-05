import time


def count_fresh():
    prod_id = []
    fresh_ranges = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if line == "": continue

            if "-" in line:
                fresh_ranges.append(
                    range(
                        int(line.split("-")[0]),
                        int(line.split("-")[1])+1
                    )
                )
            else:
                prod_id.append(int(line))

    num_fresh = 0
    for id in prod_id:
        for r in fresh_ranges:
            if id in r:
                num_fresh += 1
                break

    print(num_fresh)


start_time = time.time()
count_fresh()
print(f"Time taken for count_fresh: {time.time() - start_time:.4f} seconds")


def count_fresh_aggr():
    prod_id = []
    fresh_ranges = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if line == "": continue

            if "-" in line:
                fresh_ranges.append(
                    (
                        int(line.split("-")[0]),
                        int(line.split("-")[1])
                    )
                )
            else:
                prod_id.append(int(line))

    fresh_ranges.sort()
    aggr_ranges = []

    num_fresh = 0
    start, end = fresh_ranges[0]
    for i in range(1, len(fresh_ranges)):
        next_start, next_end = fresh_ranges[i]

        if end>=next_start:
            end = max(end, next_end)
        else:
            aggr_ranges.append(range(start, end+1))
            start, end = next_start, next_end

    aggr_ranges.append(range(start, end+1))

    for id in prod_id:
        for r in aggr_ranges:
            if id in r:
                num_fresh+=1
                break

    print(num_fresh)


start_time = time.time()
count_fresh_aggr()
print(f"Time taken for count_fresh_aggr: {time.time() - start_time:.4f} seconds")
