""" 5. Longest Palindromic SUbstring

Question:

    Given a string s, find the longest palindromic substring in s. You may
    assume that the maximum length of s is 1000.

+++

Attempt:

    Naive approach would be to consider substring of every size from 2 to
    len(s), and check for whehther the substring is a valid palindrome.

    However, the better approach would be to consider each char as a center
    point of the palindrome - such that it can only expand as far as it is
    valid. Thus, making the algorithm run in O(n^2) time complexity.

"""

class Solution:
    def expand(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == [end]:
            start -= 1
            end += 1
        return s[start+1:end]

    def longestPalindrome(self, s):
        if not s:
            return ''
        longest = ''
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            curr = s1 if len(s1) > len(s2) else s2
            longest = longest if len(longest) > len(curr) else curr
        return longest
