from typing import Tuple, List
import pdb


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "str()"

    def __repr__(self):
        return "id: {}, val: {}, next: {}\n".format(id(self), self.val, id(self.next))


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def rev(p: ListNode, q: ListNode) -> Tuple[ListNode, ListNode]:
            head = end = p
            p = p.next
            head.next = q.next
            while p != q:
                nxt = p.next
                p.next = head
                head = p
                p = nxt
            p.next = head
            head = p
            return (head, end)

        if k == 1 or not head:
            return head
        p = q = head
        # 题目说明 k 小于等于链表长度，但是仍然给出测试案例 [1], 2
        for i in range(1, k):
            if q:
                q = q.next
        if not q:
            return head
        pre_head, pre_end = rev(p, q)
        rst = pre_head
        p = q = pre_end.next
        while p:
            for i in range(1, k):
                if q:
                    q = q.next
            if q:
                cur_head, cur_end = rev(p, q)
                p = q = cur_end.next
                pre_end.next = cur_head
                pre_head, pre_end = cur_head, cur_end
            else:
                pre_end.next = p
                p = None
        return rst


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
    a = create_list([1, 2, 3, 4, 5])
    # pdb.set_trace()
    show_list(Solution().reverseKGroup(a, 1))
