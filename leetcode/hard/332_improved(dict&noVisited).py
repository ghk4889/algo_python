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
import collections

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
# but it is larger in lexical order.

# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]


################## 성능: 평균 95ms 소요  ##공간 복잡도 최악

tickets.sort()

dickets = collections.defaultdict(list)
for li in tickets:
    dickets[li[0]].append(li[1])

output = []


def dfs(fromList, stack):
    if len(stack) == len(tickets) + 1:
        output.extend(stack)
    if output:
        return
    for fromStr in fromList.copy():
        if output:
            return
        stack.append(fromStr)
        fromList.pop(0)
        dfs(dickets[fromStr], stack.copy())
        stack.pop()
        fromList.append(fromStr)


stack = ["JFK"]
for idx, first_from in enumerate(dickets["JFK"]):
    if output:
        break
    dfs(dickets["JFK"], stack.copy())

print(output)
