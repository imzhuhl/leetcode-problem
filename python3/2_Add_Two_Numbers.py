from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createList(lst: List[int]) -> ListNode:
    ln, p = None, None
    for val in lst:
        if ln == None:
            ln = ListNode(val)
            p = ln
        else:
            p.next = ListNode(val)
            p = p.next 
    return ln

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        rst, c = [], 0
        while p != None and q != None:
            tmp = p.val + q.val
            if tmp + c >= 10:
                rst.append(tmp + c - 10)
                c = 1
            else:
                rst.append(tmp + c)
                c = 0
            p = p.next
            q = q.next
        while p != None:
            if c == 1 and p.val == 9:
                rst.append(0)
            else:
                rst.append(p.val + c)
                c = 0
            p = p.next
        while q != None:
            if c == 1 and q.val == 9:
                rst.append(0)
            else:
                rst.append(q.val + c)
                c = 0
            q = q.next
        if c != 0:
            rst.append(c)
        print(rst)
        return createList(rst)
        

if __name__ == "__main__":
    l1 = createList([9, 8])
    l2 = createList([1])
    l3 = Solution().addTwoNumbers(l1, l2)
    