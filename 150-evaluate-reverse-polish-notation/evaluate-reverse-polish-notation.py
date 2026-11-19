class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for item in tokens:
            if item in '+-*/':            
                op1=stack.pop()
                op2=stack.pop()
                if item == '+':
                    stack.append(op1 + op2)
                elif item == '-':
                    stack.append(op2 - op1)
                elif item == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op2 / op1))
            else:
                stack.append(int(item))
        
        return stack[0]