import re

def count_res():
    lines = open('input.txt', 'r').readlines()

    resutls = [[0,"+"] if sign == "+" else [1,"*"] for sign in re.split(r"\s+", lines[-1].strip())]

    for line in lines[0:-1]:
        nums = re.split(r"\s+", line.strip())
        for i in range(len(nums)):
            if resutls[i][1] == "+":
                resutls[i][0] += int(nums[i])
            else:
                resutls[i][0] *= int(nums[i])

    sum = 0
    for r, _ in resutls:
        sum += r

    print(sum)

if __name__ == '__main__':
    count_res()
