# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
import collections

nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums = [1]
# Output: [[1]]

output = []


def dfs(per: list[int], restList: list[int]):
    for nextNum in restList:
        cPer = per.copy()
        cPer.append(nextNum)
        copy_rl = restList.copy()
        copy_rl.remove(nextNum)
        if not copy_rl:
            output.append(cPer)
            return
        dfs(cPer, copy_rl)

if len(nums) == 1:
    output.append(nums)
    print("return ", [nums])

for firstNum in nums:
    copy_nums = nums.copy()
    copy_nums.remove(firstNum)
    dfs([firstNum], copy_nums)

print("return ", output)
