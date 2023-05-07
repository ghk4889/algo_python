# 77. Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# 1 <= n <= 20
# 1 <= k <= n
import collections

n = 4
k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


output = []


def ff(lastNum: int, per: list[int], k: int):
    if k <= 0:
        output.append(per)
        return
    for num in range(lastNum + 1, n + 1):
        cper = per.copy()
        cper.append(num)
        ff(num, cper, k - 1)


for num in range(1, n + 1):
    ff(num, [num], k - 1)

print(output)
