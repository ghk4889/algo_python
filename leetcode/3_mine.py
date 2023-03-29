# 3. Longest Substring Without Repeating Characters
#Given a string s, find the length of the longest substring without repeating characters.

# s = "abcbabcbb"
# Output: 3

# s = "bbbbb"
# Output: 1

s = "dvdf"
# Output: 3

output = 0

substr = list()

for char in s:
    try:
        start_idx = substr.index(char)

        newLen = len(substr)

        if output < newLen:
            output = newLen

        substr = substr[start_idx+1:]
        substr.append(char)

    except:
        substr.append(char)

newLen = len(substr)
if output < newLen:
    output = newLen


print(output)


