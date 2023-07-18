class Car:
    def __init__(self,year,mpg,speed):
        self.year =year
        self.mpg =mpg
        self.speed =speed
        self.listofowners = 1

    def accelerate(self):
        return self.speed+30

    def brake(self):
        if self.speed-60>=0:
            return self.speed-60
        else:
            return 0

    #def __init__(self,mpg,speed):
     #   self.mpg =mpg
      #  self.speed = speed

    def magic(self):
        print("year " +str(self.year)+" "+"mpg "+str(self.mpg)+" "+"speed "+str(self.speed))

car1 = Car(2016,20,80)
car1.magic()
