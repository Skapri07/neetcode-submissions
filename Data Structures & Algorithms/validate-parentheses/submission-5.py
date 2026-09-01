class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s) == 1):
            return False
        for char in s:
            if(char == "["):
                stack.append("[")
            if(char == "{"):
                stack.append("{")
            if(char == "("):
                stack.append("(")
                
            if(char == ")"):
                if(stack and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
            if(char == "}"):
                if(stack and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            if(char == "]"):
                if(stack and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
                    
        if not stack:
            return True
        else:
            return False
            
                
        