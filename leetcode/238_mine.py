# 238. Product of Array Except Self

# Example 1:
# Input:
nums = [4,3,2,1,2]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

resultList = []

if nums.count(0) == 1:
    result = 1
    for i, v in enumerate(nums):
        if v == 0:
            resultList.append(1)
            continue
        resultList.append(0)
        result *= v
    resultList[nums.index(0)] = result
    print(resultList)

elif nums.count(0) > 1:
    for i in range(len(nums)):
        resultList.append(0)
    print(resultList)



for i in range(len(nums)):
    flag = False
    result = 1
    left = i - 1
    right = i + 1
    while left >= 0 and not flag:
        if nums[left] == nums[i]:
            result = resultList[left]
            flag = True
            break
        result *= nums[left]
        left -= 1
    while right < len(nums) and not flag:
        result *= nums[right]
        right += 1

    resultList.append(result)

print(resultList)
