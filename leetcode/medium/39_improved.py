# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

candidates = [2, 3, 6, 7]
target = 7
# Output: [[2,2,3],[7]]

# candidates = [2,3,5]
# target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# candidates = [2]
# target = 1
# Output: []

candidates = [3, 5, 8]
target = 11

candidates.sort()
output = []


def ff(per: list[int], restList: list[int]):
    if sum(per) > target:
        return
    elif sum(per) == target:
        output.append(per)
        return

    crList = restList.copy()
    for num in restList:
        cper = per.copy()
        cper.append(num)
        ff(cper, crList)
        crList.pop(0)

restList = candidates.copy()
for num in candidates:
    ff([num], restList)
    restList.pop(0)

print(output)
