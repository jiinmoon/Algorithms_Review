# 155 Min Stack

class MinStack:
    def __init__(self):
        self.mstk = list()
        self.stk = list()

    def push(self, x):
        self.stk.append(x)
        if self.mstk and self.mstk[-1] >= x:
            self.mstk.append(x)

    def pop(self):
        val = self.stk.pop()
        if self.mstk and self.mstk[-1] == val:
            self.mstk.pop()

    def getMin(self):
        return self.mstk[-1]

    def top(self):
        return self.stk[-1]
