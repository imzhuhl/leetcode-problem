# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(p, q):
            p.next = q.next
            q.next = p
            return q

        if not head:
            return []
        elif not head.next:
            return head
        elif head and head.next:
            rst = swap(head, head.next)

        cur = rst.next
        p = rst.next.next
        while p:
            if not p.next:
                cur.next = p
                break
            p = swap(p, p.next)
            cur.next = p
            cur = p.next
            p = p.next.next
        return rst

if __name__ == "__main__":
    pass
