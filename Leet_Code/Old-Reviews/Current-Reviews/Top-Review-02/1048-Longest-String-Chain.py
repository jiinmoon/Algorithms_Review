# 1048 Longest String Chain

class Solution:
    def longestStringChain(self, words):
        counter = collections.Counter(words)
        longest = 0

        for word in sorted(words, key=len):
            for i in range(len(word)):
                subword = word[:i] + word[i+1:]
                countSub = counter[subword] + 1
                counter[word] = max(counter[word], countSub)
                longest = max(longest, counter[word])
        
        return longest
