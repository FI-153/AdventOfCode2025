def sum_of_joltage():

    with open("input.txt") as f:

        tot = 0
        for line in f:
            digits = list(map(int, line.strip('\n')))

            max_bank_jottage = 0
            for i in range(len(digits)-1):
                tens = digits[i]
                units = max(digits[i+1:])

                curr_jottage = (tens*10) + units
                if curr_jottage > max_bank_jottage:
                    max_bank_jottage = curr_jottage

            tot += max_bank_jottage

        print(tot)

sum_of_joltage()