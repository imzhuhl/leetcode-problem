"""
快慢指针
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        flag = True
        slow, quick = head, head
        while True:
            if quick.next == None:
                flag = False
                break
            quick = quick.next
            if quick.next == None:
                flag = False
                break
            quick = quick.next

            slow = slow.next

            if quick == slow:
                break

        return flag

