# 743. Network Delay Time

# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# ui is the source node,
# vi is the target node,
# wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k.
# Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
import collections
import heapq

times = [[2, 1, 3], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# Output: 3
times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
         [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
         [3, 1, 36], [2, 3, 59]]

adjacent = collections.defaultdict(list)
for u, v, w in times:
    adjacent[u].append([v, w])

d = collections.defaultdict(list)  # 시작노드(k)부터 특정 노드까지의 현재 거리

d[k] = 0
minHeap = []
heapq.heappush(minHeap, (d[k], k))

nums = set(range(1, n + 1))


while nums and minHeap:
    d_u, u = heapq.heappop(minHeap)
    nums.discard(u) 
    for v, w in adjacent[u]:
        if v not in nums:
            # nums에서 제거된 노드를 minHeap에서 또 뽑은 경우
            continue
        elif d[v] == [] or d_u + w < d[v]:
            d[v] = d_u + w
            heapq.heappush(minHeap, (d[v], v))
            
# 노드 하나만 연결 없이 동떨어져 있는 경우엔 해당 노드가 nums에 남아있다.
# 즉, 모든 노드를 순회할 수 없는 경우이다.
if nums:
    print(-1)

print(max(d.values()))
