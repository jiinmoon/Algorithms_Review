# 1153 String Transforms Into Another String

class Solution:
    def canTransform(self, S, T):
        if S == T:
            return True
        if len(set(T)) == 26:
            return False

        charToIndicies = collections.defaultdict(list)
        for i, char in enumerate(S):
            charToIndicies[char].append(i)

        for indicies in charToIndicies.values():
            if len(set(T[i] for i in indicies)) != 1:
                return False

        return True
