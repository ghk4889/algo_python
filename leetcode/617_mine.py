# 617. Merge Two Binary Trees

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ff(p1: TreeNode, p2: TreeNode):
    if p1 and p2:
        p1.val += p2.val
        p1.left = ff(p1.left, p2.left)
        p1.right = ff(p1.right, p2.right)

    return p1 or p2
# ff(root1, root2)
# return root1 or root2