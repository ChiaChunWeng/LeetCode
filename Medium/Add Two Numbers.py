"""
    You are given two non-empty linked lists representing two non-negative integers.

    The digits are stored in reverse order, and each of their nodes contains a single digit.

    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    https://leetcode.com/problems/add-two-numbers
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        node = result
        temp = 0
        while l1 is not None or l2 is not None or temp > 0:
            if l1 is not None:
                print("L1>",temp, l1)
                print(l1)
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                print("L2>", temp, l2)
                temp += l2.val
                l2 = l2.next

            node.next = ListNode(temp % 10)  # 取個位數
            node = node.next
            temp = temp // 10  # 檢查是否要進位
        print(result.next)
        return result.next


