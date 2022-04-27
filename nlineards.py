n =8

def gcode(n):
    if n ==1:
        return ["0","1"]
    if n==0:
        return

    reans = gcode(n - 1)
    ans=[]

    for i in range(len(reans)):
        ans.append("0"+str(reans[i]))
    for j in range(len(reans)-1,-1,-1):
        ans.append("1" + str(reans[j]))
    return ans

print(gcode(n))