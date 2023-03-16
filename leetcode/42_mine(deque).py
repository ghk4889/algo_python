# 42. Trapping Rain Water

# deque를 썼다. 시간: 128ms  //  공간: 16MB
# deque는 인덱스 슬라이싱이 안 되기 때문에 알고리즘 구현이 조금 더 귀찮아진다.

from collections import deque

# Input
height = [4, 2, 3]  # Output: 6

height = deque(height)

result = 0

while height:
    start = height.popleft()
    if start == 0 or not height or height[0] >= start: continue

    endIdx = 0

    for i in range(0, len(height)):
        if height[i] >= start:
            endIdx = i
            break
        elif i == (len(height) - 1) and len(height) >= 2:
            height.reverse()
            height.append(start)

    if endIdx == 0: continue

    for i in range(endIdx):
        result += start - height[0]
        height.popleft()



print(result)
