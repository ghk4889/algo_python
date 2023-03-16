# DFS와 BFS
import sys
input = sys.stdin.readline

def dfs(n):
    visited[n] = True
    dfs_list.append(n)
    for w in sorted(adj_list[n]):
        if not visited[w]:
            dfs(w)


def bfs(n):
    visited[n] = True
    queue = [n]
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for w in sorted(adj_list[v]):
            if not visited[w]:
                visited[w] = True
                queue.append(w)


#프로그램 시작
#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
#다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
N, M, V = map(int, input().split())

#adj_list는 특정 노드가 특정 인덱스와 1:1이 된다. 즉, 인덱스가 N개만큼 있다.
# N+1인 이유는 인덱스가 1부터 시작해야 하므로.
# adj_list[1] 이 가진 리스트의 내용은 노드 1과 인접한 노드들을 의미한다.
adj_list = [[] for _ in range(N + 1)]    #[[], [], [], [], [], ..., []]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs_list = []
bfs_list = []


visited = [False] * (N + 1)       #[False, False, False, False, False, False]
dfs(V)
visited = [False] * (N + 1)
bfs(V)

print(*dfs_list)
print(*bfs_list)
