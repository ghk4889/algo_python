# 5. Longest_Palindromic_Substring

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s = "abcd"


def check1(left: int, right: int) -> str:
    while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


result = ''

for i in range(0, len(s) - 1):
    result = max(result, check1(i, i + 1), check1(i, i + 2), key=len)

print(result)
