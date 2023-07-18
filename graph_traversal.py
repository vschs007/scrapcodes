class graph:
    def __init__(self,edges):
        self.edges = edges
        self.dct ={}
        for start , end in self.edges:
            if start in self.dct:
                self.dct[start].append(end)
            else:
                self.dct[start]=[end]
       # print(self.dct)

    def getpath(self,start,end,path=[]):
        path = path +[start]

        if start == end:
            return [path]

        if start not in self.dct:
            return []

        paths = []

        for node in self.dct[start]:
            if node not in path:
                newpath = self.getpath(node,end,path)
                for p in newpath:
                    paths.append(p)
        #paths.sort()
        return paths


#routes=[("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","NY")]
n =int(input())
inputarr=[]
for i in range(n):
    inputarr.append(int(input()))

routes=[]
k = int(input())
for i in range(k):
    routes.append(list(map(int,input().split())))

print(routes)

#routes = [[2, 9], [7 ,2], [7, 9], [9, 5]]

start= int(input())
end = int(input())
gobject = graph(routes)
resarr = (gobject.getpath(start,end))
#maxList = min(resarr, key = len)
if len(resarr)>0:
    print("1")
else:
    print(("0"))
