""" 1.,5 One Away

Question:

    There are three types of edits that can be performed on strings: insert,
    remove, or replace a char. Given two strings, write a function to check
    whether a string is one (or zero) edits away.

---

The problem becomes simpler once we divide it into cases based on their length
of the strings.

We know that:

    if strings are of equal length:
        - two strings require zero or single replacement

    if strings are differ by single length:
        - two strings require either remove or insert

    if strings are differ by more than one length:
        - they cannot possibly be single edit away from one another.

Thus, we first test their lengths, then modify the strings to compare one
another.

"""


class Solution:
    def replace(self, longer, shorter):
        """ find the first different char, replace with another then compare. """
        checker = lambda x: x[0] == x[1]
        compMap = list(map, checker, list(zip(longer, shorter)))
        falseCounter = False
        for ans in compMap:
            if not ans:
                if falseCounter:
                    return False
                falseCounter = True
        return True

    def remove(self, longer, shorter):
        """ we choose to remove different char, then compare """
        i = 0
        while i < len(shorter):
            if longer[i] != shorter[i]:
                longer = ''.join(list(longer).pop(i))
                break
        return longer == shorter

    def isOneAway(self, s1, s2):
        if len(s1) > len(s2):
            longer, shorter = s1, s2
        else:
            longer, shorter = s2, s1

        # Case.1 Equal Length
        if len(longer) == len(shorter):
            # must be zero or single edit away
            return self.replace(longer, shorter)

        # Case.2 Differ by exactly one
        if abs(len(longer) - len(shorter)) == 1
            # either insert single char to shorter or remove char from longer
            return self.remove(longer, shorter)

        # Case.3 Differ by more than one
        return False # cannot be single edit away
