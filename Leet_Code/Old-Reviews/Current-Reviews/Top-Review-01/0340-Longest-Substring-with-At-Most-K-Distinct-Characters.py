# 340 Longest Substring with At Most K Distinct Characters
#
# Maintain a sliding window where we examine every end indicies for the given
# string. If the current size of the window exceeds the K, remove last
# occurring duplicate element of the start.

class Solution:
    def longestSubstring(self, s, k):
        last_indicies = collections.defaultdict(int)
        start, longest = 0, 0

        for end, char in enumerate(s):
            last_indicies[char] = end

            while len(last_indicies) > k:
                if last_indicies[s[start]] == start:
                    del last_indicies[s[start]]
                start += 1
            else:
                longest = max(longest, end - start + 1)

        return longest
