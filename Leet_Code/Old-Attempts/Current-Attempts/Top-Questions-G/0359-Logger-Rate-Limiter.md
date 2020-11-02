# 359 Logger Rate Limiter

Design a logger system that receive stream of messages along with its
timestamps, each message should be printed if and only if it is not printed in
the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the
message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

---

Simply, we implement this with a structure that allows for efficient operations
that can retrieve and update - with hashmap. It will record messages and
timestamps.

---

Python:

```python

class Logger:
    def __init__(self):
        self.d = dict()

    def shouldPrintMessage(self, msg, timestamp):
        if msg in self.d and abs(self.d[msg] - timestamp) < 10:
            return False
        self.d[msg] = timestamp
        return True
```
