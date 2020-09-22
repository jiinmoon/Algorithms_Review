# 394 Decode String

class Solution:
    def decode(self, s):
        stk = []
        num = 0
        for char in s:
            if char.isdigit():
                num *= 10 + int(char)
            elif char == '[':
                stk.append(num)
                num = 0
            elif char == ']':
                curr = list()
                tok = stk.pop()
                while not isinstance(tok, int):
                    curr = [tok] + curr
                    tok = stk.pop()
                stk += curr * tok
            else:
                stk.append(char)

        return "".join(stk)
