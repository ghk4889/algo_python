#전쟁 - 전투

# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다.
# 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
# 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다.
# 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

import sys

def bfs_power(c, a, b):
    queue = []
    queue.append((a, b))
    visited[a][b] = True
    amount = 1

    while True:
        i, j = queue.pop(0)
        if (i-1 >= 0) and (not visited[i-1][j]) and (field[i-1][j] == c):
            queue.append((i-1, j))
            visited[i-1][j] = True
            amount += 1
        if (j+1 < N) and (not visited[i][j+1]) and (field[i][j+1] == c):
            queue.append((i, j+1))
            visited[i][j+1] = True
            amount += 1
        if (i+1 < M) and (not visited[i+1][j]) and (field[i+1][j] == c):
            queue.append((i+1, j))
            visited[i+1][j] = True
            amount += 1
        if (j-1 >= 0) and (not visited[i][j-1]) and (field[i][j-1] == c):
            queue.append((i, j-1))
            visited[i][j-1] = True
            amount += 1

        if not queue: break

    return amount ** 2


def calc(c):
    totalPower = 0
    for i in range(M):
        for j in range(N):
            if (not visited[i][j]) & (field[i][j] == c):
                totalPower += bfs_power(c, i, j)
    return totalPower





#첫 번째 줄 입력
N, M = map(int, sys.stdin.readline().split())



field = [[] for _ in range(M)]  # filed = [[], [], [], [], [], []]
# field의 0번 인덱스부터 시작

print(field)

# 입력된 두 번째 줄부터 마지막 줄까지
for i in range(M):
    field[i] = list()  # 0번 인덱스부터 시작
    row = sys.stdin.readline()
    for j in range(N):
        field[i].append(row[j])

print(field)


visited = [[False for _ in range(N)] for _ in range(M)]
#[[False, False, ..., False], ... [False, False, ..., False]]

print(visited)

print(calc('W'))

print(calc('B'))
