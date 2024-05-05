class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for k in magazine:
            map[k]=map.get(k,0)+1

        for k in ransomNote:
            if k not in magazine or map[k] == 0:
                return False
            else:
                map[k] -= 1
        return True


object = Solution()

print(object.canConstruct("a",'b'))