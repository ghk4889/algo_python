# 316. Remove Duplicate Letters

# Input: s = "bcabc"
# Output: "abc"

# Input:
# s = "cbacdcbc"

# Output: "acdb"
s = "dcfcacf"

sSet = set(s)

suffix = set()
for char in sSet:
    suffixStart = s.index(char) + 1
    suffix = set(s[suffixStart:])
    if sSet.issubset(suffix):
        s = char + s[suffixStart:].replace(char, '')






# 시간 초과나는 코드
# sli = list(s)
# 
# 
# def recurv(output: list, cnt):
#     if sli[cnt] in output :
#         o1 = output.copy()
#         o1.remove(sli[cnt])
#         o1.append(sli[cnt])
#         if cnt == len(s)-1:
#             if o1 < output:
#                 return o1
#             else:
#                 return output
#         o1res = recurv(o1, cnt + 1)
#         outputles = recurv(output, cnt + 1)
#         if o1res < outputles:
#             return o1res
#         else:
#             return outputles
#     elif cnt == len(s) - 1:
#         output.append(sli[cnt])
#         return output
#     else:
#         output.append(sli[cnt])
#         return recurv(output, cnt + 1)
# 
# str=''
# print(str.join(recurv(list(), 0)))

