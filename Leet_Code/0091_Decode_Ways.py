""" 91. Decode Ways

Question:

    A message containing letters from A-Z is being encoded to numbers using the
    following mapping.

    'A' -> 1 ... 'Z' -> 26

    Given a non-empty string containing only digits, determine the total number
    of ways to decode it.

+++

Solution:

    We may use backtracking algorithm to try to find all the ways that we can
    decode the given string. At each recursive call, we should look for either
    cases where we can read a single character or double character.

    Let's suppose that we are iterating on the given string. The base-cases are
    theses: 1) the current index is within len(s) and is pointing at '0'; 2) the
    index is out of bounds. In these cases, we should return 0 since there is no
    way to decode these numbers as the decoding is not zero-indexed. i.e. 'A'
    starts with 1, not 0. Only way 0 can be used must be '10'.

    Also, when index reaches the end of the string, it means that it can be
    decoded as a string, thus a single case of 1.

    Then, the number of decoding should be recursive call of looking for single
    character case + double characters case. But in the case of double
    character, we should check whether it is within the bounds of 26.

    The backtracking algorithm used here will be exponential since we are
    looking for two additional calls for each recursive call. To reduce this, we
    should use cache - memoization method.

"""

from functools import lru_cache

class Solution:
    def numDecodings(self, s):

        @lru_cache(None)
        def backtrack(i):
            if i < len(s) and s[i] == '0' or i > len(s):
                return 0
            if i == len(s):
                return 1
            singleChar = backtrack(i+1) # consume 1 char.
            doubleChar = 0
            if 1 <= int(s[i:i+2]) <= 26:
                doubleChar = backtrack(i+2) # consume 2 chars.
            return singleChar + doubleChar

        return backtrack(0)
