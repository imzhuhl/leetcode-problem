# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path = []
        rst = []
        self.dfs(root, path, rst)

        return rst

    def dfs(self, node, path, rst):
        if node is None:
            return
        if node.left is None and node.right is None:
            path.append(node.val)
            rst.append(self.to_str(path))
            path.pop()
            return
        
        path.append(node.val)
        if node.left != None:
            self.dfs(node.left, path, rst)
        if node.right != None:
            self.dfs(node.right, path, rst)
        path.pop()
        return
        
    def to_str(self, path):
        return "->".join(map(str, path))