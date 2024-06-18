# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        carry=0

        while l1 is not None or l2 is not None or carry!=0:

            val1=l1.val if l1 is not None else 0
            val2=l2.val if l2 is not None else 0

            total=val1+val2+carry
            carry=total//10
            value=total%10

            current.next=ListNode(value)
            current=current.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next

        return dummy.next






