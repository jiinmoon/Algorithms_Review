""" 72. Edit Distance

Question:

    Given two words - word1 and word2 - find the minimum number of operations
    required to convert word1 to word2.

    3 actions permitted are (1) Insert, (2) Delete, and (3) Replace.

+++

Solution:

    We will use the recrusive method to approach this problem - that is we will
    iterate from left to right (or right to left), applying insert, delete, and
    replace. We will look for minimum that it has taken to for other word to
    reach below 0 length; then, we know the remaining distance must be removing
    which ever is left over. We also utilize the memoization technique to cache
    the each recursive results.

"""

class Solution:
    def minimum_distance(self, word1, word2):
        memo = dict()

        def find_distance(i, j)
            if i < 0 or j < 0:
                return i + 1 + j + 1
            if (i, j) in memo:
                return memo[ (i, j) ]
            if word1[i] == word2[j]:
                result = find_distance(i-1, j-1)
            else:
                result = 1 + min(
                                find_distance(i-1, j),
                                find_distance(i, j-1),
                                find_distance(i-1, j-1))
            memo[ (i, j) ] = result
            return result

        return find_distance(len(word1)-1, len(word2)-2)
