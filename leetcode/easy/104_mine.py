# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes
# along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections

root = TreeNode()

#####  sol1) bfs

if not root:
    print(0)

Q = collections.deque()
Q.append(root)
output = 0
while Q:
    output += 1
    # for parentNode in Q.copy():
    #     Q.popleft()
    # 아래처럼 개선
    for _ in range(len(Q)):
        parentNode = Q.popleft()
        if parentNode.left:
            Q.append(parentNode.left)
        if parentNode.right:
            Q.append(parentNode.right)
print(output)


#####  sol2) dfs
output2 = 0
def dfs(parent: TreeNode, level):
    if not parent:
        return True
    if dfs(parent.left, level+1) and dfs(parent.right, level+1):
        global output2
        if output2 < level:
            output2 = level
        return False
dfs(root, 1)
print(output2)


##### improved dfs

def dfs(parent, depth):
    if not parent: return depth
    return max(dfs(parent.left, depth + 1), dfs(parent.right, depth + 1))

print(dfs(root, 0))


