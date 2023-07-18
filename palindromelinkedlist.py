class Node:
    def __init__(self,head):
        self.head = head
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode


stack = []
list =['A','B','B','A']
objnode = Node('A')
for i in range(0,len(list)):
    objnode.next = Node(list[i])
    stack.append(objnode.next.head)
print(stack)

for i in range(len(list)):
    c = stack.pop(0)
    if c==objnode.head:
        objnode.head = objnode.next.head
        objnode = objnode.next
    else:
        break
if(len(stack)!=0):
    print("NO")
else:
    print("YES")








