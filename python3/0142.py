"""
NOTE
    快慢指针，假设有环
    慢指针经过 a 步进入环，经过 b 步，再过 c 步重新回到环的入口
    则快指针实际上走了 a + b + i(c+b) = 2(a + b)，其中 i 任意，因为不知道环有多大，可能快指针跑了好几圈了
    于是：
        a = c + (i-1)(c+b)
    
    c+b 刚好是一圈，也就是如果一个指针此时从起始位置出发，另一个指针从快慢指针相遇处出发，他们会在环的入口相遇
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        slow, quick = head, head
        flag = True
        while True:
            quick = quick.next
            if quick is None:
                flag = False
                break
            quick = quick.next
            if quick is None:
                flag = False
                break
            slow = slow.next
            
            if slow == quick:
                break
        
        if flag is False:
            return None
        
        p = head
        q = slow
        while p != q:
            p = p.next
            q = q.next
        return p