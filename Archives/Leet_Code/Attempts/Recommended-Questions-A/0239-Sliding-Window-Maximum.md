# 239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size
k which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.

---

We use deque data structure to maintain the maximum values for the current
sliding window. The sliding window is maintained by its indicies so that we can
easily identify the current size.

Time complexity of this algorithm would be O(n) which is same as the space
complexity required to maintain our window.

---

Java:

```java

from java.util.ArrayDeque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> result = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++) {
            while (!q.isEmpty() && nums[q.peekLast()] < nums[i])
                q.removeLast();
            q.addLast(i);
            if (q.peekFirst() <= i - k)
                q.removeFirst();
            if (i >= k - 1)
                result.add(nums[q.peekFirst()]);
        }

        return result.stream().mapToInt(i->i).toArray();
    }
}

```

Python:

```python

class Solution:
    def maxSlidingWindow(self, nums, k):
        window = collections.deque()
        result = list()
        for i, num in enumerate(nums):
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            # adding new element exceeds the size
            if window[0] <= i - k:
                window.popleft()
            # once window reaches the correct size
            if i >= k - 1:
                result.append(window[0])
        return result
```

