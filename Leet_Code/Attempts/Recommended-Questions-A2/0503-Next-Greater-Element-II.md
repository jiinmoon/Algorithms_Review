# 503. Next Greater Element II

Given a circular array (the next element of the last element is the first
element of the array), print the Next Greater Number for every element. The
Next Greater Number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly to
find its next greater number. If it doesn't exist, output -1 for this number.

---

Naive approach would be to scan across the array to left and right to find the
greater element - O(n^2) in time complexity.

We can improve upon this by using stack data structure. In stack, we hold the
previous examined indicies of the values. As we iterate on the given array in
circular fashion(upto 2 * length of nums and use modulo operation), we check
against the top of the stack. So long as the current number is greater than
what we have seen previously, we can update our result to current number.

Time and space requirements are both in O(n).

---

Java:

```java

class Solution503 {

    public int[] nextGreaterElements(int[] nums)
    {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[nums.length];
        Arrays.fill(result, -1);

        for (int i = 0; i < 2 * nums.length; i++)
        {
            int curr = nums[i % nums.length];
            while (!stack.isEmpty() && curr > nums[stack.peek()])
                result[stack.pop()] = curr;

            // only have to include upto n
            if (i < n)
                stack.push(i);
        }
        
        return result;
    }
}

```
