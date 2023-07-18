from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # last = head
        while(head and head.next):
            temp = head.next
            tmp = ListNode(temp)
            tmp.next = head
            head = head.next






