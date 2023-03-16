import sys

def maint(m):
    print("[[[%d]]]" % m)
    array = [[1, 1]]
    dline = 0

    resultList = list()
    flag = True

    for i in range(2, m):
        if flag:
            dline = i + 1
        elif dline == 2:
            # print("dline이 2인 i: ", i)
            break

        array.append([1 for col in range(dline)])
        array[1][1] = i
        for j in range(2, dline):
            if i != j:
                array[1][j] = array[0][j - 1] + array[0][j]
                xx = array[1][j]
                ij = i - j
                if xx > m:
                    flag = False
                    dline = j
                    # print("array[%d][%d] = %d" % (i, j, array[1][j]))
                    break
                elif xx == m and ij >= j:
                    resultList.append((i, j))
                    if j != (i - j):
                        resultList.append((i, ij))

        # print(array)
        array.pop(0)

    resultList.append((m, 1))
    if m != 2:
        resultList.append((m, m - 1))

    print(len(resultList))
    for n, k in resultList:
        print(n, k)


# maint(int(sys.stdin.readline()))


for ra in range(2, 100):
    print("============시작============")
    maint(ra)
    #maint(int(sys.stdin.readline()))
    print("___________________________\n")
