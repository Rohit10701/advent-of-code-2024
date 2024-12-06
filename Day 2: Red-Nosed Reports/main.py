from sortedcontainers import SortedList
from collections import Counter

f = open("./input.txt", "r")


for x in f:
    loc = list(map(int, x.split()))
