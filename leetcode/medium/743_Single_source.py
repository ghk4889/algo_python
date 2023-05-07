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

times = [[2, 1, 3], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# Output: 3
# times = [[1,2,1]]

dictimes = collections.defaultdict(list)
for u, v, w in times:
    dictimes[u].append([v, w])

d = collections.defaultdict(list)

d[k] = 0

que = collections.deque()
que.append(k)

while que:
    u = que.pop()
    for v, w in dictimes[u]:
        if d[v] == [] or d[u] + w < d[v]:
            d[v] = d[u]+w
            que.append(v)

if len(d.keys()) != n:
    print(-1)

print(max(d.values()))

