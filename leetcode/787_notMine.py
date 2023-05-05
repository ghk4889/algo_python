# 787. Cheapest Flights Within K Stops

# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei]
# indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k.
# return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.

# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst

import collections
import heapq
import math

n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
#Output: 700


adjacent = collections.defaultdict(list)
for fromi, toi, pricei in flights:
    adjacent[fromi].append((pricei, toi))

minHeap = []
heapq.heappush(minHeap,(0, src, k+1))

d = [[math.inf]*(k+2) for _ in range(n)]


while minHeap:
    p, node, k = heapq.heappop(minHeap)
    if node == dst:
        print(p)
    if k > 0:
        for pricei, adjNode in adjacent[node]:
            if d[adjNode][k-1] > p + pricei:
                d[adjNode][k-1] = p + pricei
                heapq.heappush(minHeap, (pricei + p, adjNode,k - 1))


print(-1)





