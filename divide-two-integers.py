# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using dummy node
        temp = ListNode(0, head)
        # 2 pointers , one at start other at offset of n from first
        first = temp
        second = temp
        while second.next and n:
            n -= 1
            second = second.next

        # now diff bw first and second is n places, so when second
        # will go to the end of list , fist wil be one node back to the node which needs to be deleted
        while second.next:
            first = first.next
            second = second.next

        # now deleting the node
        first.next = first.next.next

        return temp.next

