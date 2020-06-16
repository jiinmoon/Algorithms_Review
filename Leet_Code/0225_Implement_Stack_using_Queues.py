""" 225. Implement Stack using Queues """

class CustomStack:
    """ We require only as single queue; we append what we pop. """
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.append(val)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return not len(self.queue)
