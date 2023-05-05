# 543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode()

diameter = 0


def dfs(parent: TreeNode):
    if not parent:
        return 0
    leftDepth = dfs(parent.left)
    rightDepth = dfs(parent.right)
    global diameter
    if leftDepth + rightDepth > diameter:
        diameter = leftDepth+rightDepth
    return max(leftDepth, rightDepth) + 1


dfs(root)
print(diameter)
