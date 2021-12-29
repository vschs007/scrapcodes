n =int(input())
while(n):
    s = input()
    if (len(s)<=10):
        print(s)
    elif len(s)>10:
        sz = len(s)-2
        print(str(s[0])+str(sz)+str(s[-1]))
    n-=1
