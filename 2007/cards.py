# BIO round 1 q1 - 24/24
from math import comb
from itertools import combinations

def solve(nums):
    res = 0
    # get points from pairs with identical values
    for i in range(1, 11):
        if nums.count(i) > 1:
            res += int(comb(nums.count(i), 2))
    # get points from groups summing to 15
    for c in list(combinations(nums, 1)):
        if sum(c) == 15: res += 1
    for c in list(combinations(nums, 2)):
        if sum(c) == 15: res += 1
    for c in list(combinations(nums, 3)):
        if sum(c) == 15: res += 1
    for c in list(combinations(nums, 4)):
        if sum(c) == 15: res += 1
    for c in list(combinations(nums, 5)):
        if sum(c) == 15: res += 1

    return res

nums = [int(i) for i in input().split(' ')]
print(solve(nums))