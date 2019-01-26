import itertools
from bisect import *
def getFibs(size):
    yield 1
    currFib = 1
    nextFib = 1
    while nextFib < size:
        currFib, nextFib = nextFib, currFib + nextFib
        yield nextFib

fibs = list(getFibs(10**100))
while True:
    start, end = map(int,input().split(" "))
    if start == 0 and end == 0:
        break
    left = bisect_left(fibs, start)
    right = bisect_right(fibs, end)
    print(right - left)
