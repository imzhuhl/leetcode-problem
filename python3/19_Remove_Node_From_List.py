# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fst, mid, last = None, None, head
        for i in range(n-1):
            last = last.next
        mid = head
        while last.next != None:
            last = last.next
            mid = mid.next
            if not fst:
                fst = head
            else:
                fst = fst.next
        if not fst:  # remove head node
            head = head.next
        else:
            fst.next = mid.next
        return head



        