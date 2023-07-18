# # Enter your code here. Read input from STDIN. Print output to STDOUT
# def dectobin(n, k):
#     str = ""
#     while (n > 0):
#         digit = n % k
#         n = int(n / k)
#         str = chr(digit + ord('0')) + str
#     return str
#
#
# def ispalindrome(k):
#     if k == k[::-1]:
#         return True
#     else:
#         return False
#
#
# n, k = map(int, input().split(" "))
# ans = 0
# for i in range(1, n + 1):
#     if ispalindrome(str(i)):
#         tmp = dectobin(i, k)
#         if ispalindrome(tmp):
#             ans+=i
#
# print(ans)
#East or west,    CSE is the best.
#
#

# s = input()
# lst = list(map(str,s.replace(","," ").replace(";"," ").split(" ")))
# cnt=0
# for k in lst:
#     if k not in ["",',',";","."]:
#         cnt+=1
# print(cnt)
# print(lst)
def f(x,y,z):
    return x+y+z

print(list(enumerate("python")))
