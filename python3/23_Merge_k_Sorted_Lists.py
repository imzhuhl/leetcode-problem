from typing import List
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(ln1: ListNode, ln2: ListNode) -> ListNode:
            if not ln1:
                return ln2
            if not ln2:
                return ln1
            ln3, p = None, None
            while ln1 and ln2:
                if ln1.val <= ln2.val:
                    tmp = ListNode(ln1.val)
                    ln1 = ln1.next
                else:
                    tmp = ListNode(ln2.val)
                    ln2 = ln2.next
                if ln3:
                    p.next = tmp
                    p = p.next
                else:
                    ln3 = p = tmp
            if ln1:
                p.next = ln1
            if ln2:
                p.next = ln2
            return ln3

        def div(lists: List[ListNode]) -> ListNode:
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            return merge(div(lists[:mid]), div(lists[mid:]))

        return div(lists)


def create_list(lst: List[int]) -> ListNode:
    ln, p = None, None
    for val in lst:
        if ln is None:
            ln = ListNode(val)
            p = ln
        else:
            p.next = ListNode(val)
            p = p.next
    return ln


def show_list(ln: ListNode):
    while ln:
        print(ln.val, end=" ")
        ln = ln.next
    print()


if __name__ == "__main__":
    a = create_list([1, 4, 5])
    b = create_list([1, 3, 4])
    c = create_list([2, 6])
    x = [a, b, c]
    show_list(Solution().mergeKLists(x))

