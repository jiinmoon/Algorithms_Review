""" 150. Evaluate Reverse Polish Notation """

class Solution:
    def eval(self, operator, x, y):
        result = 0
        if operator == '+':
            result = x + y
        elif operator == '-':
            result = y - x
        elif operator == '*':
            result = x * y
        else:
            result = int(y / x)
        return result

    def evaluateRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            # is token an operator or operand?
            if token not in '+-*/':
                stack.append(token)
            else:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(self.eval(token, num1, num2))
        return stack[-1] if stack else 0
