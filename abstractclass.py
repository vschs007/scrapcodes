from abc import ABC , abstractmethod
class Shape(ABC):
    def area(self,side):
        pass
    def pmt(self,side):
        pass

class square(Shape):
    def area(self,side):
        return side*side


ob1 = square()
print(ob1.area(5))
