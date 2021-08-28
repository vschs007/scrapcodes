# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def rec(ListNode):
#     answer=[]
#     while ListNode.next is not None:
#         print(ListNode.val)
#         ListNode.next= None
#     #return answer
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for k in lists:
            curr = k 
            while(curr):
                res.append(curr.val)
                curr = curr.next
        res.sort()
        #making a linkedlist
        cur = temp  = ListNode(0)
        while res:
            e = res.pop(0)
            cur.next = ListNode(e)
            cur = cur.next
        return temp.next
        
                
                

            
    
        
        
        
