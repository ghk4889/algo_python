# 42. Trapping Rain Water

# list를 썼다. 시간 184ms  //  공간 15.5MB

# Input
height = [4, 2, 3]  # Output: 6

result = 0

while height:
    start = height.pop(0)
    if start == 0 or not height or height[0] >= start: continue

    endIdx = 0

    for i in range(0, len(height)):
        if height[i] >= start:
            endIdx = i
            break
        elif i == (len(height)-1) and len(height) >= 2:
            height.reverse()
            height.append(start)

    if endIdx == 0: continue
    result += sum(list(map(lambda x: start - x, height[:endIdx])))

    del height[:endIdx]

print(result)