
def solution(rows, columns, queries):

    # baseMatrix, answer 생성
    baseMatrix = []
    answer = []

    for row in range(1, rows+1):
        startColumn = columns * (row - 1) + 1
        baseMatrix.append(list(range(startColumn, startColumn+columns)))

    # 위 for문을 한 줄로 정리하면 아래와 같음 (2가지 종류)
    # baseMatrix = [(list(range(columns * (row - 1) + 1, columns * (row - 1) + 1+columns))) for row in range(1,rows+1)]
    # board = [[i + (j) * columns for i in range(1, columns + 1)] for j in range(rows)]

    # print(baseMatrix)

    # query to src
    query = [2,2,5,4]
    for query in queries:
        src = [i - 1 for i in query]  # src == [1, 1, 4, 3]
        # print(src)
        a, b, c, d = src[0], src[1], src[2], src[3]

        # rotate & find minimum
        min = tmpSwap = baseMatrix[a][b]  # start point

        # rotate 1 (src[0] row)
        for col in range(b, d):
            tmp = baseMatrix[a][col + 1]
            baseMatrix[a][col + 1] = tmpSwap
            tmpSwap = tmp
            min = tmp if min > tmp else min

        # rotate 2 (src[3] col)
        for row in range(a, c):
            tmp = baseMatrix[row + 1][d]
            baseMatrix[row + 1][d] = tmpSwap
            tmpSwap = tmp
            min = tmp if min > tmp else min

        # rotate 3 (src[2] row)
        for col in range(d, b, -1):
            tmp = baseMatrix[c][col - 1]
            baseMatrix[c][col - 1] = tmpSwap
            tmpSwap = tmp
            min = tmp if min > tmp else min

        # rotate 4 (src[1] col)
        for row in range(c, a, -1):
            tmp = baseMatrix[row - 1][b]
            baseMatrix[row - 1][b] = tmpSwap
            tmpSwap = tmp
            min = tmp if min > tmp else min

        # print("min: ", min)
        answer.append(min)
        # print(baseMatrix)

    # print(answer)
    return answer


solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])

#result : [8, 10, 25]