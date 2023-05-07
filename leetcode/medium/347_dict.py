# 347. Top K Frequent Elements

# Given an integer array nums and an integer k
# return the k most frequent elements. You may return the answer in any order.
import collections

nums = [1, 1, 1, 2, 2, 3,3,3]
k = 2
# Output: [1,2]  or  [2,1]

# 105 ms
# dict()와 dict.items() 메서드를 알고 있어야 나오는 풀이.
frequency = {}

for num in nums:
    if num not in frequency:
        frequency[num] = 1
    else:
        frequency[num] = frequency[num] + 1

frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

result = list(frequency.keys())[:k]

print(result)
