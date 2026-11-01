class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        mp = {}
        ans = 0

        while r < len(s):
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                mp[s[r]] += 1

            while(r-l +1)-max(mp.values()) > k:
                mp[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans


obj = Solution()
print(obj.characterReplacement("ABAB",2))



