# 687. Longest Univalue Path
# Given the root of a binary tree, return the length of the longest path,
# where each node in the path has the same value.
# This path may or may not pass through the root.
# The length of the path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode()

outset = {0, }


def dfs(parentVal: int, node: TreeNode):
    if not node:
        return 0
    leftV, rightV = dfs(node.val, node.left), dfs(node.val, node.right)
    outset.add(leftV + rightV)
    if parentVal != node.val:
        return 0
    return max(leftV + 1, rightV + 1)


dfs(None, root)

print(max(outset))










