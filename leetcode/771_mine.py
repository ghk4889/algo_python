#771. Jewels and Stones


# jewels = "z"
# stones = "ZZ"

# Output: 0
import collections

jewels = "aA"
stones = "aAAbbbb"
# Output: 3

#### sol1 : defaultdict 활용 ####

# stone_dict = collections.defaultdict(int)
#
# for char in stones:
#     stone_dict[char] += 1
#
#
# output = 0
# for char in jewels:
#     output += stone_dict[char]
#
# print(output)


#### sol2) String 내장 함수 사용 ####

output = 0
for char in jewels:
    output += stones.count(char)
print(output)




