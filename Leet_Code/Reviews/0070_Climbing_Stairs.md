70 Climbing Stairs
==================

Question:
---------

Each time you can either climb 1 or 2 steps. If so, then how many different
ways can you reach to top of the stairs?

Solutions:
----------

This is a fib sequence problem essentially where if we generalize it, the total
number of ways to arrive at any stiars depends upon previous i-1 and i-2
values. The recursive solution is generally worse as it is O(2^n) algorithm
where each function recursively spawns two another. It can be improved by using
memoization technique but iterative approach can solve this problem without
having to rely on such methods in linear time.


Codes:
------

Go:

```go
func climbStairs(n int) int {
    if n <= 0 {
        return 0
    }
    if n <= 2 {
        return n
    }
    prev, curr = 1, 2
    for i := 3; i < n+1; i++ {
        curr, prev = curr + prev, curr
    }
    return curr
}
```
---

**Source:**

LeetCode: [Climbing-Stairs](https://leetcode.com/problems/climbing-stairs/)
