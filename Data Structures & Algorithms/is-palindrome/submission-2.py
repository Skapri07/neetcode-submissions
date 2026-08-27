import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", x)
        i = 0
        j = len(cleaned_text) - 1

        while(i < j):
            if(cleaned_text[i] != cleaned_text[j]):
                return False
            i += 1
            j -= 1
        return True
