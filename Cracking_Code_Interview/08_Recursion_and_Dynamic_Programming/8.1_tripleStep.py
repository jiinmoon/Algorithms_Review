""" 8.1 Triple Step


Question:

    A child is running up a staircase with n steps and can hop either 1, 2, or 3
    steps at a time. Implement a method to count how many possible ways the
    child can run up the stairs.

---

This dynamic programming problem is a spin on the Fibonacci problem. Hence, the
brute force approach of naive recursive way would be O(3^n) time complexity
(since each function call branches to 3 more calls).

To optimize upon this, we can use temp cache to store the previously computed
value instead of calling the functions to save time. You can either use simple
array if keys are in 1 .. n or HashMap structure such as Dict.

"""
