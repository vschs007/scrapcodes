class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchile(self,data):
        if data ==self.data:
            return
        if data < self.data:
            #left me add krna hai
            if self.left:
                self.left.addchile(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.addchile(data)
            else:
                self.right = bst(data)

    def inorder(self):
        elements=[]
        if self.left:
            elements+= self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder()

        return elements

def buildtree(elements):
    root = bst(elements[0])
    for i in range(1,len(elements)):
        root.addchile(elements[i])
    return root

numbers = [17,4,1,20,9,23,18,34]

ntree = buildtree(numbers)

print(ntree.inorder())
