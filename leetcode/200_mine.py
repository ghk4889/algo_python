# 200. Number of Islands

# An island is formed by connecting adjacent lands horizontally or vertically.

# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
# Output: 3

stack = list()

N = len(grid[0])
M = len(grid)
visited = [[False for _ in range(N)] for _ in range(M)]


def dfs(row, col):
    if visited[row][col] or grid[row][col] != "1":
        return
    visited[row][col] = True
    if row - 1 >= 0:
        dfs(row - 1, col)
    if col + 1 < N:
        dfs(row, col + 1)
    if row + 1 < M:
        dfs(row + 1, col)
    if col - 1 >= 0:
        dfs(row, col - 1)


output = 0

for row, rowList in enumerate(grid):
    for col, v in enumerate(rowList):
        if v == "1" and not visited[row][col]:
            dfs(row, col)
            output += 1

print(output)

# 이 문제는 visited를 두지 않아도 된다.
# 이미 방문한 노드의 값을 "1"이 아닌 다른 값으로 바꿔주면서 진행하면 공간 복잡도가 더 개선된다.
