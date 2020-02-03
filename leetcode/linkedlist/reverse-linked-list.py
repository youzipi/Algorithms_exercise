"""
encoding=utf-8
_author = youzipi
date = 2019/1/16
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _head = head

        prev = head
        cur = head.next
        next = head.next.next
        if cur.next:
            cur.next, cur, prev = prev, cur.next, cur

        _head.next = None
        return cur


if __name__ == '__main__':
    head = ListNode(1)
    tail = head

    for i in range(2, 6):
        tail.next = ListNode(i)
        tail = tail.next

    s = Solution()
    result = s.reverseList(head)
    print(result)
