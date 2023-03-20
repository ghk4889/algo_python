# 739. Daily Temperatures

# Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1,1,4,2,1,1,0,0]

from collections import deque

output = [0 for i in range(len(temperatures))]
stack = deque()

for idx, temper in enumerate(temperatures):

    for i in range(len(stack)):
        if temper > stack[0][1]:
            pl = stack.popleft()
            output[pl[0]] = idx-pl[0]
        else:
            break

    stack.appendleft((idx, temper))

print(output)




