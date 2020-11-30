# 84. Largest Rectangle Histrogram

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

---

To determine the largest rectangle area that we have thus far, we have to look
far from the current position so long as the previous bar is at least equal in
its height compared to the current height. Implementing this naively, we have
to iterate back each time at the position hence would be O(n^2) in time
complexity.

We can make an improvement by using stack; stack will maintain the list of
heights that we have seen thus far; and reduce the top as we are examining the
current area. This will use O(n) in space, but will reduce the time complexity
down to O(n) as well.

---

Java:

```java

class Solution84 {
    
    public int largestRectangle(int[] heights)
    {
        // add 0 in the end as a guard for len(1)
        int[] hist = new int[heights.length + 1];
        for (int i = 0; i < heights.length; i++)
            hist[i] = heights[i];

        Stack<Integer> stack = new Stack<>();
        result = 0;

        for (int i = 0; i < hist.length; i++)
        {
            // at each position, look as far behind as possible
            while (!stack.isEmpty() && hist[stk.peek()] >= hist[i]
            {
                int height = hist[stack.pop()];
                int width = (stack.isEmpty()) ? i : i - stack.peek() - 1;
                result = Math.max(result, height * width);
            }
            stack.append(i);
        }
        return result;
    }
}

```
