# 142. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is
a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

---

We can think of this problem as an extension of finding the longest palindromic
substring - expanding about the middle element. But here, we can combine with
DP record.

    Let DP[i] be a minimum cut to be made up to i-th string s. Then we have
    following:

        As we expand about the mid-point in our substring, DP[r] where r is the
        right pointer in the substring can be updated as a minimum cut value
        that we have found in previous DP[r] OR mimum cut we have found at
        DP[l] which is the left pointer in the substring + 1. Thus, min cut at
        left is updated whenever we found the palindrome by the prevous min cut
        from prefix upto r.

Originally our dp is initailized with increasing index - 1 as these are minimum
cuts required at their indicies if only palindromic substrings that we can find
are the length of 1, which indicates that we require as many cuts as the length
of the string - 1.

Time complexity would be O(n^2) due to having to expand on each of the
characters and O(n) to maintain our dp array.

---

Java:

```java

class Solution142 {
    
    private char[] chars;
    private int[] dp;
    
    public int minCut(String s) 
    {    
        this.chars = s.toCharArray();
        this.dp = new int[this.chars.length + 1];
        
        for (int i = 0; i < this.chars.length + 1; i++)
            this.dp[i] = i - 1;
        
        for (int i = 0; i < this.chars.length; i++)
        {
            expand(i, i);
            expand(i, i+1);
        }
        
        return this.dp[this.dp.length-1];
    }
    
    private void expand(int start, int end)
    {
        while (start >= 0 && end < this.chars.length && this.chars[start] == this.chars[end])
        {
            this.dp[end + 1] = Math.min(this.dp[end + 1], 1 + this.dp[start]);
            start--;
            end++;
        }
    }
}

```
