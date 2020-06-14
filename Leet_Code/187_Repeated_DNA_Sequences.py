""" 187. Repeated DNA Sequences

Question:

    Find all the 10 letter-long sequences that occur more than once in a DNA
    molecule.

+++

Solution:

    There are many finding needle in the haystack algorithms; in this case, we
    are trying to find **all** patterns that repeat more than once. Hence, we
    would use record structure while exaiming all the 10 letter sequences.

"""

class Solution:
    def findRepeatedSequences(self, s):
        record = set()
        result = set()
        for i in range(len(s) - 9):
            currSeq = s[i:i+10]
            # have we seen current sequence beforehand?
            if currSeq in record:
                result.add(currSeq)
            else:
                record.add(currSeq)
        return result
