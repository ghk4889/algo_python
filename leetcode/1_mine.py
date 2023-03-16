# 1. Two Sum
nums = [3, 3]
target = 6

#output : [0,1]  인덱스를 반환

dic = {}

for i, v in enumerate(nums):
    dic[v] = i

for i, v in enumerate(nums):
    if target-v in dic and i != dic[target-v]:
        print(i, dic[target-v])


