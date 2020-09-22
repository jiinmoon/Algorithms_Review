# 809 Expressive Words

class Solution:
    def isExpressive(self, s, words):
        def helper(word):
            chars, counts = list(), list()
            count = 1
            for i, char in enumerate(word):
                if i == len(word)-1 or word[i+1] != char:
                    chars.append(char)
                    counts.append(count)
                    count = 0
                count += 1
            return chars, counts

        charS, countS = helper(s)
        total = 0
        for word in words:
            charW, countW = helper(word)
            if charW != charS:
                return -1

            for cw, cs in zip(countW, countS):
                if cw > cs: break
                if cw < cs and cs < 3: break
            else:
                total += 1

        return total
