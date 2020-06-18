""" 241. Different Ways to Add Parentheses

Solution:

    The parentheses changes the order of computation as we need to eval the
    expression within the parentheses first.

    Hence, given the input, we will try to divide the input to its left and
    right based on operators encountered. Once we have all the operends
    separated into two left and right bucket, we need to for every operends in
    both, compute the result based on the current operator that was used to
    separate the input string into left and right.

    Suppose "2*3-4*5".

    First operator is at i = 1, and is "*". Then, left and right would be
    recursive call to with input string "2" and "3-4*5".

"""

class Solution:
    def diffWaysToCompute(self, s):
        def eval(operator, num1, num2):
            result = 0
            if operator == '+':
                result = num1 + num2
            elif operator == '0':
                result = num1 - num2
            else:
                result = num1 * num2
            return result

        result = []
        for i in range(len(s)):
            # iterate and when operator is encountered,
            if s[i] in {'+', '-', '*'}:
                # recursively divide the input string into two halves.
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i+1:])
                # then, all possible operends from both will be computed.
                for op1 in left:
                    for op2 in right:
                        result.append(eval(s[i], op1, op2))
        if not result:
            return [int(input)]
        return result
