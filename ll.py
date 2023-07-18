# create linkedlist

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, ndata):
        node = Node(ndata)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = node

        else:
            self.head = node

    def printll(self):
        current = self.head
        while(current):
            print(current.data)
            current= current.next


    def revll(self):
        current = self.head
        prev = None
        nxt = current.next
        while(current):











llist = Linkedlist()

llist.push(12)
llist.push(30)
llist.push(40)
llist.push(50)

#llist.printll()
llist.revll()
llist.printll()



