# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
import collections

numCourses = 2
prerequisites = [[1, 0]]
# Output: True

numCourses = 20
prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
# Output: False
numCourses = 5
prerequisites =[[1,4],[2,4],[3,1],[3,2]]


######### 평균 소요 시간 : 133ms // 공간복잡도 최악

di_wf = collections.defaultdict(list)

for wantNum, firstNum in prerequisites:
    di_wf[wantNum].append(firstNum)


def findDeepNecessary(wantNum_, stack: set):
    if wantNum_ in stack:
        return False
    stack.add(wantNum_)
    firstList = di_wf[wantNum_]
    if not firstList:
        return True
    for firstNum in firstList:
        if not findDeepNecessary(firstNum, stack.copy()):
            return False
    di_wf[wantNum_] = []
    return True


for wantNum in list(di_wf)[::-1]:
    for first in di_wf[wantNum]:
        stack = {wantNum}
        if not findDeepNecessary(first, stack.copy()):
            print(False)
            break
    di_wf[wantNum] = []

print(True)
print(di_wf)
