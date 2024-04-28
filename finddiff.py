class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map = {}
        for c in s:
            # add to hashmap
            map[c] = map.get(c, 0) + 1

        for c in t:
            if c not in map or map[c] == 0:
                return c
            map[c] -= 1

