def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    for i in range(1, 10 ** 6):
        if '0' not in str(i) and multiplyList(map(int, str(i))) >= n - len(str(i)) + sum(map(int, str(i))):
            print('1' * (n - len(str(i))), i, sep='')
            #break