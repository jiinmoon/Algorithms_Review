""" 127. Word Letter

Question:

    Given two words and a dictionary of word list, find the length of shortest
    transformation sequence from beginWord to endWord such that:

        1. only a single char can be changed each time.
        2. each transformed word must exist in the word list.

+++

Solution:

    We will treat this problem as a graph traversal problem such that BFS can be
    used to find whether there exists a path from beginWord to the endWord.

"""

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        dictionary = set(wordList)
        dictionary.add(beginWord)

        if endWord is not in dictionary:
            return 0

        # dictionary will work also as a visited list.
        # each word that has been visited will be marked off.
        queue = [ beginWord ]
        depth = 0
        while queue:
            depth += 1
            m = len(queue)
            for _ in range(m):
                currWord = queue.pop(0)
                # the next words to explore would be a current word with a
                # single char replaced - we will examine all 26 possibilities
                # for each index.
                for i in range(len(currWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if currWord[i] == c:
                            continue
                        newWord = currWord[:i] + c + currWord[i+1:]
                        if newWord == endWord:
                            return depth + 1
                        # newWord is a neighbour. add to queue for visit.
                        if newWord in dictionary:
                            queue.append(newWord)
                            dictionary.remove(newWord)
        return 0 # there is no path.

