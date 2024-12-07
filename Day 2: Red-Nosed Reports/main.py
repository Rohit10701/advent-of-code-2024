from sortedcontainers import SortedList
from collections import Counter

f = open("./input.txt", "r")

records = []
safe_records_count = 0
for x in f:
    records.append(list(map(int, x.split())))

def evaluate_records(record):
    # incresing
    flag = False
    inc_flag = True
    last_rec = record[0]-2
    for r in record:
        if last_rec > r  or 1 > abs(last_rec - r) or abs(last_rec - r) > 3:
            inc_flag = False
            break
        last_rec = r

    # descresing
    dec_flag = True
    last_rec = record[0]+2
    for i, r in enumerate(record):
        if last_rec < r  or 1 > abs(last_rec - r) or abs(last_rec - r) > 3:
            dec_flag = False
            break
        last_rec = r
    return 1 if (dec_flag or inc_flag) else 0

# 1 3 2 3 5 
"""
if 1 remove 2 then it ll blow up gotta remove first 3
"""

for record in records:
    safe_records_count += evaluate_records(record)
tmp = safe_records_count
print("Q1", safe_records_count)
# Q2

for record in records:
    for i in range(len(record)):
        if evaluate_records(record[:i]+record[i+1:]):
            safe_records_count += 1
            break
    
print("Q2", safe_records_count - tmp)
