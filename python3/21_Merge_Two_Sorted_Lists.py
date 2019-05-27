# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        l3, p = None, None
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l2 = l2.next
            if not l3:
                l3 = p = tmp
            else:
                p.next = tmp
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return l3
