from os import environ
from functools import reduce
from itertools import groupby
from math import prod

lines = open("input_test.txt" if environ.get("DEBUG") else "input.txt").read().splitlines()

print(
    sum(
        reduce(((int.__mul__, int.__add__)[c[-1] == "+"]), map(int, c[:-1]))
        for c in zip(*[l.split() for l in lines if l.strip()])
    )
)

cols = ["".join(c) for c in zip(*[l.ljust(max(len(x) for x in lines)) for l in lines])]


def do_block(g):
    return (sum if any(c.endswith("+") for c in g) else prod)(
        int(c[:-1].replace(" ", "")) for c in g if c[:-1].strip()
    )


print(
    sum(
        do_block(list(g))
        for k, g in groupby(cols, key=lambda x: not x.strip())
        if not k
    )
)