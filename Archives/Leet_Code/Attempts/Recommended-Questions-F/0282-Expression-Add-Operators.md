# 282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all
possibilities to add binary operators (not unary) +, -, or * between the digits
so they evaluate to the target value.

---

Using recursion, we try to build the expression as we iterate from left to
right on the given string of numbers. If the evaluation of the expression or
final current index reached the end of the length of given string, we can add
current path to our result. Otherwise, at every possible insertion point
starting from the current index, we try to add each binary operators. As we
have to consider "*", we also have to maintain the value of the previously
added num as well. Since there are 3 operators to insert at each positions, the
total time complexity would be O(4^(n-1)).

---

Python:

```python

class Solution:
    def addOperators(self, num, target):
        def helper(path, pathSum, left, prev):
            # end of expression
            if path == target or left == len(num):
                result.append(path)

            # start from each index "right" of left index
            # add each operators
            for i in range(left, len(num)):
                # ignore leading zero
                if i > left and num[left] == '0':
                    break

            # current num segment to consider
            currSeg = num[left:i+1]
            currVal = int(currSeg)

            # start of path; do not add any operators
            if left == 0:
                helper(path + currSeg, currVal, i + 1, currVal)
            else:
                # 3 possible ways to add the operators
                # if it is "*", we have to subtract the previous val added
                helper(path + "+" + currSeg, pathSum + currSeg, i + 1, currVal)
                helper(path + "-" + currSeg, pathSum - currSeg, i + 1, -currVal)
                helper(path + "*" + currSeg, pathSum - prev + prev * currVal, i + 1, prev * currVal)

        result = list()
        helper("", 0, 0, 0)
        return result
```


