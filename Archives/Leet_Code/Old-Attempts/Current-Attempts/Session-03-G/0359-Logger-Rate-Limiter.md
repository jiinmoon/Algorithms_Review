# 359 Logger Rate Limiter

Use hashmap to store msg: timestamps.

---

Python:

```python

class Logger:
    def __init__(self):
        self.d = dict()

    def log(self, msg, timestamp):
        if msg in self.d and timestamp - self.d[timestamp] < 10:
            return False
        self.d[msg] = timestamp
```
