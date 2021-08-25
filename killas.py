class School:
    count = 0
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        School.count+=1


student1 = School('vivek','56')
student2 = School('vdivek','564')
student3 = School('vigvek','566')

print(School.count)

