
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        record = []
        self.dfs(root, 0, record)
        return record

    def dfs(self, node: TreeNode, level: int, record: List[List[int]]):
        if node == None:
            return
        
        if level >= len(record):
            record.append([])
        record[level].append(node.val)
        
        self.dfs(node.left, level + 1, record)
        self.dfs(node.right, level + 1, record)


def ints2tree(ints: List[int]) -> TreeNode:
    n = len(ints)
    if n == 0:
        return None

    root = TreeNode(ints[0])
    queue = [root]
    i = 1
    while len(queue) != 0:
        node = queue[0]
        queue = queue[1:]

        if i < n and ints[i] != None:
            node.left = TreeNode(ints[i])
            queue.append(node.left)
        i += 1

        if i < n and ints[i] != None:
            node.right = TreeNode(ints[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    order = [3, 9, 20, None, None, 15, 7]
    root = ints2tree(order)
    # print('{}, {}, {}'.format(root.val, root.left.val, root.right.left.val))
    s = Solution()
    rst = s.levelOrder(root)
    print(rst)

