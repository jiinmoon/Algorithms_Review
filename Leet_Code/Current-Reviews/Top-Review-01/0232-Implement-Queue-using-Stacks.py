# 232 Implement Queue using Stacks

class StackQueue:
    def __init__(self):
        self.pop_stk = list()
        self.push_stk = list()
        self.top = None

    def enqueue(self, x);
        if not self.push_stk:
            self.top = x
        self.push_stk.append(x)

    def dequeue(self):
        if not self.pop_stk:
            while self.push_stk:
                self.pop_stk.append(self.push_stk.pop())
        return self.pop_stk.pop()

    def peek(self):
        if self.pop_stk:
            return self.pop_stk[-1]
        return self.top

    def empty(self):
        return not (len(self.pop_stk) + len(self.push_stk))

