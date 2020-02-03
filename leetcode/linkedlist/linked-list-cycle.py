"""
encoding=utf-8
_author = youzipi
date = 2019/1/16
"""

"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
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
    head = ListNode(2)
    tail = head

    for i in [0,]:
        tail.next = ListNode(i)
        tail = tail.next

    s = Solution()
    result = s.reverseList(head)
    print(result)
