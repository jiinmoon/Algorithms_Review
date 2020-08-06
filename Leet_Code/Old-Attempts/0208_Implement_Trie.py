""" 208. Implement Trie

Question:

    Implement a trie with insert, search and startsWith methods.

+++

Solution:

    Trie tree can simply be implemented as a hashmap structure - where we would
    simply add char for insertion and its value as another hashmap structure
    such that would form another depth of the Trie tree. Hence, we can iterate
    on this Trie structure by continusouly retrieving the values.

"""

class CustomeTrie:
    def __init__(self):
        self.root = dict()

    def insert(self, word):
        trie = self.root:
        for char in word:
            # char may already be present within the Trie.
            if char not in trie:
                trie[char] = dict()
            trie = trie[char]
        # we need to mark the end of word.
        trie['#'] = word

    def search(self, word):
        trie = self.root
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return '#' in trie

    def startsWith(self, prefix):
        trie = self.root
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True

