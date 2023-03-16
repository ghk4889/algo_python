# 15. 3Sum
from collections import deque

########Copy로 배열을 통 복사 하는 과정 때문에 타임오버됨.###########
### -> 투 포인터 방식으로 nums의 복사본을 만들지 않고 처리함.

# Input
# nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

nums = [0,0,0]

nums.sort()
print(nums)

results = list()

if nums[0] > 0 or nums[len(nums) - 1] < 0 or len(nums) < 3:
    pass

for idx, start in enumerate(nums):
    if start > 0: break
    if idx > 0 and start == nums[idx-1]: continue

    left = idx + 1
    right = len(nums)-1

    while left < right:

        nowSum = start + nums[left] + nums[right]
        if nowSum == 0:
            results.append([start, nums[left], nums[right]])
            while left != len(nums) - 1 and nums[left] == nums[left + 1]:
                left += 1
            while right != 0 and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif nowSum < 0:
            left += 1
        elif nowSum > 0:
            right -= 1


print(results)

