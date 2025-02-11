# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        - start with base case first
        - make sure you see what the sentinel node is
        -
        """
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        head = ListNode(-1)
        curr = head

        carry = 0
        while l1 or l2 or carry != 0:
            # total = l1.val + l2.val + carry
            # l3.val, carry = divmod(total, 10)
            # l3 = l3.next
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            totalS = l1val + l2val + carry

            # outS, carry = divmod(totalS, 10)

            carry = totalS // 10
            newNode = ListNode(totalS % 10)

            # newNode = ListNode(outS)
            curr.next = newNode
            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


if __name__ == "__main__":
    assert Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert Solution().addTwoNumbers([0], [0]) == [0]
    assert Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]
