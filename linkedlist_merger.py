class listnode:
    def __init__(self,val=0,next = None ):
        self.val =val
        self.next = next
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
res=[]
for test in lists:
    curr = test
    while(curr):
        res.append(curr.val)
        curr = curr.next
print(res)
 B
cur = dummy = ListNode(0)
        while tracker:
            e = tracker.pop(0)
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
