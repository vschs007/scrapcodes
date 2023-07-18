def dec(func):
    def wrap():
        print(func[::-1])
        func()
    return wrap



@dec
def prn(s):
    print(s)


prn()