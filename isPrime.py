def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

arrp=[]
for j in range(2,1000):
    if(isPrime(j)):
        arrp.append(j)
print(arrp)
