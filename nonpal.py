t= int(input())
while(t):
    res="abcdefghijklmnopqrstuvwxyz"
    str=""
    n = int(input())
    turns = n//26 +1
    if turns <2:
        for i in range(n):
            str+=chr(i+97)
    else:
        for i in range(turns):
            str+=res

    print(str[0:n])
    t-=1
#print(len("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi"))

