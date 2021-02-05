# 735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

---

Here, we can user stack data structure to look back at the previous asteroid
that we have examined and compare against the current. Until we can cancel out
the asteroid, we remove the top of the stack; otherwise, we add the current and
move onto next.

Time complexity and space both be O(n);

---

Python:

```python

class Solution735:

    def asteroidCollision(self, asteroids):
        
        result = list()

        for curr in asteroids:
            while result and result[-1] > 0 and curr < 0:
                eval = result[-1] - curr
                # current cancels out with previous; remove previous and current
                if not eval:
                    result.pop()
                    break
                # previous is greater than current; ignore current
                elif eval > 0:
                    break
                # previous is smaller than current; remove previous and add current
                else:
                    result.pop()
            # otherwise, current is valid
            else:
                result.append(curr)

        return result
```

