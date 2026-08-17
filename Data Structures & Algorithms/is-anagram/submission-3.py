class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for num in s:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for num in t:
            if num  not in seen:
                return False
            else:
                seen[num] -= 1
            if seen[num] < 0:
                return False
            
        return True
    