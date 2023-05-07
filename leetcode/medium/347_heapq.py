# 347. Top K Frequent Elements

# Given an integer array nums and an integer k
# return the k most frequent elements. You may return the answer in any order.
import collections
import heapq

nums = [1, 1, 1, 2, 2, 3,3,3]
k = 2
# Output: [1,2]  or  [2,1]

numset = set(nums)

output = []

memli = list()

# 각 요소의 갯수 구하기 mine  - 1700 ms
for num in numset:
    heapq.heappush(memli, (-nums.count(num), num))

# 각 요소의 갯수 구하기 counter 활용  - 95 ms
freqs = collections.Counter(nums)

for f in freqs:
    heapq.heappush(memli, (-freqs[f], f))

# output 완성
for _ in range(k):
    output.append(heapq.heappop(memli)[1])

print(output)

