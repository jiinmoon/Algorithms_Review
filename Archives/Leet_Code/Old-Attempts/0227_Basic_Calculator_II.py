""" 227. Basic Calculator II

Solution:

    The main problem is taking care of the operator precedence. We can approach
    this problem in many ways but simplest way is to utilize the stack.

"""

class Solution:
    def calculate(self, s):
        stack, op, num = [], '+', 0
        s += '+'
        for char in s:
            if char.isdigit():
                num = (num * 10) + int(char)
            elif char == ' ':
                pass
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(stack.pop() / num)
                op = char
                num = 0
        return sum(stack)
