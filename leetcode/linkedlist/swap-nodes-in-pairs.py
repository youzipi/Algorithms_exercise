"""
encoding=utf-8
_author = youzipi
date = 2019/1/16
"""

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        _head = head.next
        cur = head

        while cur.next:
            cur.next, cur.next.next, cur = cur.next.next, cur, cur.next.next
        return _head


if __name__ == '__main__':
    head = ListNode(1)
    tail = head

    for i in range(2, 6):
        tail.next = ListNode(i)
        tail = tail.next

    s = Solution()
    result = s.swapPairs(head)
    result_head = result
    while result_head:
        print(result_head.val)
        result_head = result_head.next
