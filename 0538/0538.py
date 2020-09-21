'''
Author       : Zhu Honglin
Date         : 2020-09-21 12:58:47
LastEditTime : 2020-09-21 14:10:11
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total_sum = 0
        
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.total_sum += node.val
            node.val = self.total_sum
            dfs(node.left)

        dfs(root)
        return root
    
        