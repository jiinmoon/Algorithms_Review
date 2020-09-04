359 Loger Rate Limiter
======================

Design a logger system that receive stream of messages along with its
timestamps, each message should be printed if and only if it is not printed in
the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the
message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

---

We use a hashmap to record the message : timestamp; check whether message is in
the map and its stored timestamp and the current timestamp is within the 10
second range.

---

Python: hash-map approach.

```python
class Logger:
    def __init__(self):
        self.d = dict()
    
    def shouldPrintMessage(self, timestamp, message):
        if message in self.d and abs(timestamp-self.d[message]) < 10:
            return False
        self.d[message] = timestamp
        return True
```
