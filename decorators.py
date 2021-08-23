import time

def timec(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        test = func(*args,**kwargs)
        endtime = time.time()
        print((endtime-start) *100)
        return  test
    return wrapper

@timec
def ge(arr):
    s = arr[0]
    e = arr[1]
    res=[]
    for i in range(s,e):
        res.append(i)
    return res


result = ge([1,20000])
print(result[2])
