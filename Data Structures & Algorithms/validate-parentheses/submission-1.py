class Solution:
    def isValid(self, s: str) -> bool:
        while("()" in s or "{}" in s or "[]" in s):
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                s = s.replace("[]","")
        if(len(s) == 0):
            return True
            

        return False
        