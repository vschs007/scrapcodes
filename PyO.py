class student:
    count=0
    def __init__(self):
        student.count=student.count+1

    def display(self):
        print(student.count)

st=student()
print(st.count)
