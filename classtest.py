class person:
    def __init__(self,name):
        self.name =name
    def sayhi(self):
        print("my name is ",self.name)
p1 = person("vivek")

print(p1.name)
p1.sayhi()