# 359 Logger Rate Limiter

class Logger:
    def __init__(self):
        self.q = dict()

    def log(self, msg, timestamp):
        if msg in self.d and timestamp - self.d[msg] < 10:
            return False
        self.d[msg] = timestamp
