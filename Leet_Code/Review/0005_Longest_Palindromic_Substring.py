""" 5. Longest Palindromic Substring

Question:

    Given a string s, find the longest palindromic substring in s. You may
    assume that the maximum length of s is 1000.

+++

Solution:

    One approach would be to consider each and every substring of various
    lengths to check which has the longest substring. But this exhaustive
    search is very costly in time complexity due to nested nature, resulting in
    a O(n^3). 

    We can make a modification that is better - instead of considering every
    start and end points, we consider every index as a centre of the
    palindrome. This is an O(n^2) time complexity.

    For linear time complexity, there exists an algorithm called Manacher's
    algorithm; but it is non-trivial algorithm that is much too complex to come
    up with on your own.

"""

class Solution:
    def expand(self, s, start, end):
        while start > 0 and end < len(s) and s[start] == s[end]:
            start += 1
            end -= 1
        return s[start+1:end]

    def findLongestPalindrome(self, s):
        if not s: return 0
        longest = 0
        for i in range(len(s)-1):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            longest = max(longest, len(s1), len(s2))
        return longest
