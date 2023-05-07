# 332. Reconstruct Itinerary

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# from_i.length == 3
# to_i.length == 3
# from_i and to_i consist of uppercase English letters.
# from_i != to_i

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
# but it is larger in lexical order.
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

################## 성능: 평균 204 ms 소요  ## 공간 복잡도는 평균

tickets.sort()

visited = [False for _ in range(len(tickets))]

stack = ["JFK"]
output = []


def dfs(fromStr: str):
    if all(visited):
        output.extend(stack.copy())
        return
    if output:
        return
    for idx, li in enumerate(tickets):
        if li[0] == fromStr and not visited[idx]:
            stack.append(li[1])
            visited[idx] = True
            dfs(li[1])
            stack.pop()
            visited[idx] = False



for start_jfk in tickets:
    if output:
        break
    if start_jfk[0] == "JFK":
        startIDX = tickets.index(start_jfk)
        visited[startIDX] = True
        stack.append(start_jfk[1])
        dfs(start_jfk[1])
        stack.pop()
        visited[startIDX] = False



print(output)












