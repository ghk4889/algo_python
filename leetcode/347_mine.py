# 347. Top K Frequent Elements

# Given an integer array nums and an integer k
# return the k most frequent elements. You may return the answer in any order.
import collections

nums = [1, 1, 1, 2, 2, 3,3,3]
k = 2
# Output: [1,2]  or  [2,1]

# 1700 ms 걸림
# heapq만 도입하는 버전과 소비 시간이 똑같음. 각 요소들을 count하는 과정에서 시간을 많이 뺏김.

numset = set(nums)

output = []

memli = list()

for num in numset:
    memli.append((num, nums.count(num)))

memli.sort(key=lambda n: -n[1])

for i in range(k):
    output.append(memli[i][0])

print(output)

