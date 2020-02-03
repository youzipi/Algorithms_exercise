"""
encoding=utf-8
_author = youzipi
date = 2019/1/16
"""
"""
876. 链表的中间结点

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 

提示：

给定链表的结点数介于 1 和 100 之间。
"""

"""
使用 快慢指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        step_1_p = step_2_p = head
        while step_2_p and step_2_p.next:
            step_2_p = step_2_p.next.next
            step_1_p = step_1_p.next

            # print('step_2=', step_2_p.val)
            # print('step_1=', step_1_p.val)

        return step_1_p


if __name__ == '__main__':
    head = ListNode(1)
    tail = head

    for i in [2, 3, 4, 5, ]:
        tail.next = ListNode(i)
        tail = tail.next

    s = Solution()
    result = s.middleNode(head)
    print(result.val)
