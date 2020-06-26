""" 165. Compare Version Numbers

Question:

    Compare two version numbers ver1, and ver2.

    If ver1 > ver2, return 1; if ver1 < ver2, return -1; else, 0.

    Assume that the version strings are non-emptry and contain only digits and .
    character.

    The '.' character is simply sequence separator, not a decimal.

+++

Solution:

    Let's break down step by step what needs to happen.

    First, we would like to tokenize the string based on the '.' character such
    that it is much easier to work with.

    Second, we do not have a gurantee that two version string would be of same
    length, thus we would try to add space holders to shorter string.

    Now, we can simply compare from the beginning, as higher first value
    indicates greater version number.

"""

class Solution:
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')

        # v1 is shorter end.
        if len(v1) > len(v2):
            v1, v2 = v2, v1

        # append 0 to balance uneven length.
        while len(v1) != len(v2):
            v1.append('0')

        for curr1, curr2 in zip(v1, v2):
            if int(curr1) > int(curr2):
                return 1
            elif int(curr1) < int(curr2):
                return -1
        return 0

