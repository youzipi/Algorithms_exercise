"""
encoding=utf-8
_author = youzipi
date = 16/12/10
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        nums = []
        while a:
            if a.val in nums:
                return a
            else:
                nums.append(a.val)
                a = a.next


s = Solution()
result = s.detectCycle([0, 1, 2, 3, 4, 3])
print(result)
