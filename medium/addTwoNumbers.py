from typing import Optional
from utils.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        """
        Problem: Add Two Numbers ; leetcode #2
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        Example 2:

        Input: l1 = [0], l2 = [0]
        Output: [0]
        Example 3:

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
        """
        cur = resHead = ListNode()
        carry = 0

        while l1 or l2 or carry:
            l1Val = 0 if not l1 else l1.val
            l2Val = 0 if not l2 else l2.val
            curSum = l1Val + l2Val + carry
            curDig = curSum % 10
            carry = curSum // 10
            cur.next = ListNode(curDig)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next

        return resHead.next

        # def extractNum(head):
        #     if not head:
        #         return 0
        #     return head.val + 10 * extractNum(head.next)

        # sumLists = extractNum(l1) + extractNum(l2)
        # newHead = cur = ListNode(sumLists % 10)
        # sumLists //= 10
        # while sumLists:
        #     cur.next = ListNode(sumLists % 10)
        #     sumLists //= 10
        #     cur = cur.next
        # return newHead
