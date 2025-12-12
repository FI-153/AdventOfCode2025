import re

# Answer the question: how many areas are big enough to host all the presents given that each one has a fixed maximum
# area of 3x3?

if __name__ == "__main__":
    max_present_area = 3*3

    areas = re.findall(r"^\d+x\d+:\s+.*$", open("input.txt").read(), re.MULTILINE)

    print(
        sum(
            [
                (int(area.split("x")[0]) * int(area.split(":")[0].split("x")[1])) >= max_present_area
                *
                sum(list(map(int, area.split()[1:])))

                for area in areas
            ]
        )
    )