""" 58. Length of Last Word

Question:

    Given a string s consists of upper/lower-case alphabets and empty space
    characters ' ', return the length of last word in the string.

"""

class Solution:
    def length_of_last_word(self, s):
        return len(s.strip().split(' ')[-1])

