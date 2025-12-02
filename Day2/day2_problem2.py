def find_base_and_repetitions():
    with open('input.txt', 'r') as file:
        ranges = next(file).split(',')

        acc = 0
        for r in ranges:
            splits = r.split('-')

            begin = int(splits[0])
            end = int(splits[1])

            for i in range(begin, end+1):
                if i<10: continue

                i_s = str(i)
                for group_size in range(1, len(i_s)//2+1):

                    if len(i_s)%group_size!=0: continue

                    base = i_s[:group_size]
                    repetitions = len(i_s)//group_size
                    if base*repetitions == i_s:
                        acc+=i
                        break

        print(acc==70187097315)

import re
def using_regex():
    with open('input.txt', 'r') as file:
        ranges = next(file).split(',')

        # Same as the one in part 1 but now the "+" makes it so
        # we're trying to match the substring multiple times over the string
        regex = re.compile(r"^(\d+)\1+$")

        acc = 0
        for r in ranges:
            begin, end = map(int, r.split('-'))

            for i in range(begin, end + 1):
                if i < 10: continue

                if regex.match(str(i)):
                    acc+=i

        print(acc==70187097315)

using_regex()