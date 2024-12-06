from sortedcontainers import SortedList
from collections import Counter

f = open("./input.txt", "r")

locationA = SortedList()
locationB = SortedList()

for x in f:
    loc = list(map(int, x.split()))
    locationA.add(loc[0])
    locationB.add(loc[1])

# part1

diff = 0
for i in range(len(locationA)):
    diff += abs(locationA[i] - locationB[i]) 
print(diff)



# part2

counterB = Counter(locationB)
score = 0
for i in range(len(locationA)):
    score += locationA[i]*counterB[locationA[i]]
print(score)

f.close()

