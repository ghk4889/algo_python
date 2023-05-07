# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets(the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

#1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

nums = [0]
# Output: [[],[0]]

nums = [1, 2, 3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


output = [[]]

def ff(per: list[int], restList: list[int]):
    output.append(per)
    crList = restList.copy()
    for num in restList:
        cper = per.copy()
        cper.append(num)
        crList.pop(0)
        ff(cper, crList)


cnums = nums.copy()
for num in nums:
    cnums.pop(0)
    ff([num], cnums)

print(output)




