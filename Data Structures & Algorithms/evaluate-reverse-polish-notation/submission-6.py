class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #initialize the stack
        #lets go from begining each elements at a time okk
            #keep on pushing every number to stack unless you see operation.
                  #if you see operation then  pop the remaining number and perform that operaion
        stack = []
        for x in tokens:
            if x not in {"+", "-", "*", "/"}:
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if(x == "+"):
                    result = a + b
                elif(x == "*"):
                    result = a * b
                elif(x == "-"):
                    result = b - a
                else:
                    result = int(b / a)
                stack.append(result)
        return stack[-1]