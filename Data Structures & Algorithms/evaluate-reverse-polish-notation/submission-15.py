class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set({'*', '/', '+', '-'})
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '*':
                    stack.append(op1 * op2)
                elif t == '+':
                    stack.append(op1 + op2)
                elif t == '-':
                    stack.append(op1 - op2)
                else:
                    stack.append(int(op1 / op2))
        return stack[-1]