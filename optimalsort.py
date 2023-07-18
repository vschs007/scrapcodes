# t = int(input())
# while(t):
#     n = int(input())
#     res=[]
#     arr = list(map(int,input().split()))
#     sortedarr = sorted(arr)
#     if arr == sortedarr:
#         print("0")
#         continue
#     t-=1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=""
        currlen=0
        maxlen=0
        for c in s:
            if c in ans:
                i = ans.index(c)
                ans = ans[i+1:]
                currlen = len(ans)
                #maxlen=max(currlen,maxlen)
            #else:
            ans = ans+c
            currlen+=1
            maxlen = max(currlen,maxlen)
        return maxlen


s= Solution()
print(s.lengthOfLongestSubstring("aab"))

