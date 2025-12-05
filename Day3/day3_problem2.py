def sum_of_joltage_original():

    with open("input.txt") as f:

        tot = 0
        for line in f:
            digits = list(map(int, line.strip('\n')))

            stack = [digits[0]]
            removals = len(digits)-12
            for i in range(len(digits)):
                while removals > 0 and stack and stack[-1] < digits[i]:
                    stack.pop()
                    removals -= 1

                stack.append(digits[i])

            digits_str = map(str, stack)
            numbers = ""
            for digit in digits_str: numbers += digit
            tot += int(numbers)

        print(tot)


def sum_of_joltage():
        with open("input.txt") as f:
            tot = 0
            for line in f:
                line = line.strip()
                if not line: continue

                # Convert to int list (though char comparison would also work)
                digits = list(map(int, line))

                # FIX 1: Start with an empty stack
                stack = []
                removals = len(digits) - 12

                # Iterate through digits directly
                for digit in digits:
                    while removals > 0 and stack and stack[-1] < digit:
                        stack.pop()
                        removals -= 1
                    stack.append(digit)

                # FIX 2: Truncate stack to exactly 12 items
                # (Essential for cases like '98765...' where nothing is popped)
                final_sequence = stack[:12]

                # FIX 3: Pythonic string joining
                tot += int("".join(map(str, final_sequence)))

            print(tot)


if __name__ == "__main__":
    sum_of_joltage()