Jumping on the Clouds
=====================

We simply try to play the game - starting from index 0, we try to reach the end
by trying out 1 and 2 steps. First, try to take furthest step (2); if not
possible, take 1 step. If both are not possible to perform, then we break out.

---

Python:

```python
class Cloud:
    SAFE = 0

def jumpingOnClouds(c):
    total, pos = 0, 0
    while True:
        if pos+2 < len(c) and c[pos+2] == Cloud.SAFE:
            pos += 2
        elif pos+1 < len(c) and c[pos+1] == Cloud.SAFE:
            pos += 1
        else:
            break
        total += 1
    return total
```
