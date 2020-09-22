# 796 Number of Matching Subsequences

class Solution:
    def numberMatchingSubseq(self, S, words):
        headToBody = collections.defaultdict(list)
        headToBody["#"] = words
        res = 0

        for char in S:
            suffixes = headToBody[char]
            del headToBody[char]

            for suffix in suffixes:
                if not suffix:
                    res += 1
                    continue
                headToBody[suffix[0]].append(suffix[1:])

        return res
