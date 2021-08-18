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
routes = [(1, 2), (2, 3), (3, 5), (4, 5)]

start= 1
end = 5
gobject = graph(routes)

print(gobject.getpath(start,end))