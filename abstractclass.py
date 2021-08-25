from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self,side):
        pass
    @abstractmethod
    def pmt(self,side):
        pass

class square(Shape):
    def area(self,side):
        return side*side



sh= Shape()

#ob1 = square()
#print(ob1.area(5))
