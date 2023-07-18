t= int(input())
while(t):
    n = int(input())
    if n%7==0:
        print(n)
    else:
        if len(str(n))==2:
            rem = n%10
            if rem >= 3:
                print(n-(n%7))
            else:
                print(n-(7-(n%7)))
        elif len(str(n))==3:
            rem =n%100
            if rem>=3:
                print(n - (n % 7))
            else:
                print(n - (7 - (n % 7)))
    t-=1