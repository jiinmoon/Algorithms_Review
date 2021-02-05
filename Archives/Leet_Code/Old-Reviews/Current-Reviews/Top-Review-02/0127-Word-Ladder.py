# 127 Word Ladder

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if not end in words:
            return -1

        length = 1
        f, b, visited = {begin}, {end}, {}
        g = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].add(word)

        while f:
            if f & b:
                return length

            newf = set()
            for word in f:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    nextWords = g[wild]
                    nextWords -= visited
                    newf |= nextWords

            f = newf
            length += 1

            if len(f) > len(b):
                f, b = b, f

        return -1
