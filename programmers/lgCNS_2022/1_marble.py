from itertools import combinations


def calcAns(evenMarbles):
    ans = []
    tmp = []
    # allCase는 좌우 갯수가 동일한 모든 경우들
    allCase = list(set(combinations(evenMarbles, len(evenMarbles) // 2)))
    print("allCase: ", allCase)

    # 왼쪽과 오른쪽은 값이 동일하다. 이 값은 전체 합의 절반이다.
    # allCase는 피봇 왼쪽 또는 오른쪽 둘 중 한 쪽(oneWay) 요소들의 묶음. (아직은 후보들이고 정답은 아래 for문에서 찾는다.)
    oneWaySum = sum(evenMarbles) // 2

    # li1의 요소(튜플)들 중에서 요소(튜플) 내부 요소의 합이 oneWaySum인 요소(튜플) 2개를 찾으면 됨.
    # 여기서 베스트 조합을 찾는 것이 핵심.
    # ex) [1, 1, 2, 2, 2, 2, 3, 3] 라는 marbles가 들어온 경우.
    # *best: [1,1,3,3], [2,2,2,2] *worst: [1,2,2,3] [1,2,2,3] -> 사전 순서 때문
    # 따라서 제일 작은 요소가 가장 많이 있는 조합을 뽑아야 된다.

    # 1. min 값과 min 값의 갯수를 파악
    min = evenMarbles[0]  # marbles는 정렬된 상태로 들어옴
    minCnt = evenMarbles.count(min)

    # 2. 모든 조합을 뽑아서 tmp에 담아둠
    for oneTuple in allCase:
        if sum(oneTuple) == oneWaySum:
            tmp.append(oneTuple)

    # 만들 수 있는 조합이 없는 경우
    if not tmp: return

    print("tmp: ", tmp)

    # 3. tmp에 담아 둔 조합들 중에서 min 값을 가장 많이 갖고 있는 조합 하나를 찾음.
    flag = False
    for i in range(minCnt, 0, -1):
        for oneTuple in tmp:
            if oneTuple.count(min) == i:
                ans.append(oneTuple)
                flag = True
                break
        if flag: break

    cpy = evenMarbles.copy()
    for j in ans[0]:
        cpy.remove(j)

    ans.append(cpy)

    # 4순위: 순서 맞추기 - 좌우 갯수는 무조건 동일하다.
    for i in range(0, len(ans[0])):
        if ans[0][i] < ans[1][i]:
            break
        elif ans[0][i] > ans[1][i]:
            ans[0], ans[1] = ans[1], ans[0]
            break

    ans = [y for x in ans for y in x]
    print("ans: ", ans)
    return ans

def findAns(marbles):

    print("findAns(marbles)의 marbles = ", end=" ")
    print(marbles)

    ans = []
    tmp = []

    # 1. 피봇 좌우의 갯수 및 합은 무조건 같아야 됨. (다를 경우 그냥 피봇 하나만 두어야 함.)
    # 2. 구슬을 배제하는 연산은 바깥에서 진행하고 이 함수(findAns)를 호출할 때 반드시 다 들어가야 되는 구슬들만 marbles 매개변수로 넘겨줌.
    # 1, 2번에 의해 현재 들어온 marbles의 요소가 짝수인 경우 피봇이 절대 있으면 안 됨. 홀수일 경우 피봇이 무조건 있어야 됨.

    if len(marbles) == 1 : return None

    if len(marbles) % 2 == 0 :
        # 그리고 좌우 각각의 합은 항상 같으므로(짝수 아니면 홀수) 모든 요소의 총 합(짝+짝 or 홀+홀)은 항상 짝수임.
        if sum(marbles) % 2 != 0 : return None

        ans = calcAns(marbles)
        if not ans : return None
        return ans



    # marbles가 홀수인 경우. 홀수일 경우 피봇이 무조건 있어야 함.
    else:
        # pivot의 중복을 없애기 위해 중복된 요소를 모두 제거한 리스트 noDupList
        noDupList = list(set(marbles))
        print("noDupList: ", noDupList)

        for pivot in noDupList:

            rmPivotList = marbles.copy()
            rmPivotList.remove(pivot)

            print("  - pivot 값:", pivot)
            print("  - pivot을 제외한 rmPivotList: ", rmPivotList)

            # 좌우 각각의 합은 항상 같아야 하므로(짝수 아니면 홀수) 모든 요소의 총 합(짝+짝 or 홀+홀)은 항상 짝수임.
            if sum(rmPivotList) % 2 != 0 : continue

            ans = calcAns(rmPivotList)
            if not ans : continue

            print("len(ans): ", len(ans))
            ans.insert(len(ans)//2, pivot)
            return ans

    print("last ans: ", end="")
    print(ans)

    return None



def solution(marbles):
    answer = []
    marbles.sort()
    tmp = []
    for rmCnt in range(0,len(marbles)):
        rms = list(set(combinations(marbles, rmCnt))) # 입력 리스트의 모든 조합을 구한다.(중복은 set으로 제거)
        print("\n-----------------------")
        print("@@@", rms, end="@@@\n-----------------------\n")
        for rmList in rms:
            cpy = marbles.copy()
            for oneMarble in rmList:
                cpy.remove(oneMarble)

            answer = findAns(cpy)
            if answer :
                print("!!!!!끝!!!!!")
                return answer

    answer = [max(marbles)]

    return answer


# a = solution([1,2,3,4,4])
# a = solution([5,5,4,1])
# a = solution([3,9,7,5])
a = solution([7,3,1])
# a = solution([2,1,1,2,3,3,2,2])
print("\n\n 결과: ", a)
