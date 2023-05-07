# 20. Valid Parentheses

# Input: s = "()"
# Output: true

# Input:
s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

# s= "([]){}"

# condition: s consists of parentheses only '()[]{}'.

#ASCII 코드
# (  40     ) 41    [ 91    ] 93    { 123   }125
stack = []
for i in range(0, len(s)):
    if s[i] in ")]}":
        if stack and stack.pop() + s[i] in "(){}[]":
            continue
        else:
            False

    stack.append(s[i])

if stack:
    print(False)

print(True)

