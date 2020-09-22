# 127 Word Ladder
#
# To find the shortest route, we can use BFS - to be precise, we can use
# bi-directional BFS since we know the goal in order to avoid the worst case
# (exploring on one end where it is more sparse compared to another).

class Solution:
    def wordLadder(self, begin, end, words):
        words = set(words)
        if not end in words:
            return 1

        length = 1
        front, back = { begin }, { end }
        visited = set()
        g = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                wild = word[:i] + "." + word[i+1:]
                g[wild].add(word)

        while front:
            if front & back:
                return length

            newfront = set()
            for word in front:
                visited.add(word)
                for i in range(len(word)):
                    wild = word[:i] + "." + word[i+1:]
                    nextWords = g[wild]
                    nextWords -= visited
                    newfront |= nextWords

            front = newfront
            length += 1

            if len(front) > len(back):
                front, back = back, front

        return -1
