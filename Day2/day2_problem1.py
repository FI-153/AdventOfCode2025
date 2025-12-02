def search_for_echoes():
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

                if len(i_s) & 1:
                    # If the number has odd length there cannot be a mirrored part
                    continue

                mid = len(i_s)//2
                if i_s[:mid] == i_s[mid:]:
                    acc+=i

        print(acc==54234399924)

import re
def using_regex():
    with open('input.txt', 'r') as file:
        ranges = next(file).split(',')

        # Match the previous substring once over the string
        # It is greedy so it starts trying to match the whole string
        # then tries 1 char less and so on
        regex = re.compile(r"^(\d+)\1$")

        acc = 0
        for r in ranges:
            begin, end = map(int, r.split('-'))

            for i in range(begin, end + 1):
                if i < 10: continue

                if regex.match(str(i)):
                    acc+=i
        print(acc==54234399924)

using_regex()