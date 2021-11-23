def bmi(h,w):
    bmi =702.151*w/(h*h)
    bmi = round(bmi,1)
    return bmi

p = int(input("How many people: "))
height_arr=[None]*p
weight_arr = [None]*p

#taking input
for i in range(p):
    print(f"Enter height and weight for person({i+1})")
    h = int(input("H (inch): "))
    w = int(input("w (lbs): "))
    height_arr[i]=h
    weight_arr[i]=w
#sending values to function
for i in range(p):
    res = bmi(height_arr[i],weight_arr[i])
    print(f"BMI of person({i+1}): {res}")

