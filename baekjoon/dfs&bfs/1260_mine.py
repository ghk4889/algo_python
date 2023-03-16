# DFS와 BFS
import sys

#now는 현재 차례의 노드
def dfs(graph, now):
    result.append(now)
    nowlist = graph[now]

    for next in nowlist:
        if result.count(next):
            continue
        else:
            dfs(graph, next)


def bfs(graph, now):
    result.append(now)
    queue = list()
    queue.extend(graph[now])
    graph[now].clear()

    while True:
        if not queue: break
        next = queue.pop(0)
        if result.count(next): continue
        result.append(next)
        queue.extend(graph[next])
        graph[next].clear()



#입력 받기
firstLineList = sys.stdin.readline().split()

startNode = int(firstLineList[2])  # 시작 노드




#입력 받은 값으로 graph 만들기

graph = dict()

while True:
    eachLineList = sys.stdin.readline().split()
    if not eachLineList:
        break

    a = int(eachLineList[0])
    b = int(eachLineList[1])

    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

# graph의 각 키 별 리스트를 sort하기
for key in graph.keys():
    graph[key].sort()


result = list()

if startNode not in graph:
    print(startNode)
    print(startNode)
    exit()

dfs(graph.copy(), startNode)

print(*result)

result = list()

bfs(graph.copy(), startNode)
print(*result)
