# Valid IP Addresses

Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are
numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings
are sorted in order)

---

Here, we use recursive backtracking to generate all possible valid IPv4s. To do
so, we carry the current segment count, candidates left, and path we are
building. Once we have exhuasted all the candidates and segment count reaches
4, we can add this to our result. Otherwise, we recursively consider single
digit case, two digit case, and three digit cases.

Time and space complexity will be constant as size of possible string must be
fixed.

---

Python:

```python

class Solution:

    def restoreIPAdresses(self, A):

        result = []

        def helper(segCount, candidates, path):
            
            if not candidates:
                if segCount == 4:
                    result.append(".".join(path))
                return

            elif segCount > 3:
                return
            else:
                
                helper(segCount + 1,    \
                    candidates[1:],     \
                    path + [candidates[0]])
                
                if 10 <= int(candidates[:2]) <= 99:
                    helper(segCount + 1,    \
                        candidates[2:],     \
                        path + [candidates[:2]]

                if 100 <= int(candidates[:3]) <= 255:
                    helper(segCount + 1,    \
                        candidates[3:],     \
                        path + [canddiates[:3]])

        helper(0, A, [])

        return result

```

