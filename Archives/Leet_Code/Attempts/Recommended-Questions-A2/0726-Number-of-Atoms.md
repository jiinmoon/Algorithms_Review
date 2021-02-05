# 726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more
lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is
greater than 1. If the count is 1, no digits will follow. For example, H2O and
H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example,
H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also
a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following
form: the first name (in sorted order), followed by its count (if that count is
more than 1), followed by the second name (in sorted order), followed by its
count (if that count is more than 1), and so on.

---

Due to parentheses we have to consider recursively evaluating the expressions
in between the parentheses to retrieve the each of the atom found and update
its count.

To do so, we recursively traverse on each index; each character encountered
will be of following cases:

(1) Current character is letter; then it is either beginning of the new atom
name (is uppercase) or extends current atom name (is lowercase). If it is a new
atom, then we record the atom name that we have built so far and its count into
hashmap.

(2) Current character is digit; it represents the count of current atom
associated. As there can be multiple digits, we extend the previous counts.

(3) Current character is open parentheses. This marks the beginning of the
expression which we have to update all our counts within the expressions by the
number following the closed parentheses. We recurse to get the expression and
its count. Then, find the number after the closed parentheses (i.e. 8 in
"(...)8"), and update our current record of atom and counts.

(4) Current character is closed parentheses. This marks the end of our
expression; record what we have built so far and return the counter.

---

Python:

```python

class Solution:

    def numAtoms(self, formula):

        def helper(left):
            name, count, i = None, 0, left
            record = collections.defaultdict(int)

            while i < len(formula):
                curr = formula[i]

                if curr.isupper():
                    if name:
                        record[name] += count if count else 1
                        count = 0
                    name = curr
                elif curr.islower():
                    name += curr
                elif curr.isdigit():
                    count = count * 10 + int(curr)
                elif curr == "(":
                    innerCounter, i= helper(i + 1)
                    num = 0
                    while i < len(formula) - 1 and formula[i+1].isdigit():
                        num = num * 10 + int(formula[i+1]):
                        i += 1
                    for innerName, innerCount in innerCounter.items():
                        record[innerName] += innerCount * (num if num else 1)
                else:
                    if name:
                        record[name] += count if count else 1
                    return (record, i)
                i += 1
        
        formula = ["("] + formula + [")"]
        result, _ = helper(0)
        return "".join(name + (str(count) if count else "") for name, count in result.items())
```
