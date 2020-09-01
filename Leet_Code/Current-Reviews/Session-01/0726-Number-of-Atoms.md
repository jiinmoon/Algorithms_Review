726 Number of Atoms
===================

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more
lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count
is greater than 1. If the count is 1, no digits will follow. For example, H2O
and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example,
H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also
a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following
form: the first name (in sorted order), followed by its count (if that count is
more than 1), followed by the second name (in sorted order), followed by its
count (if that count is more than 1), and so on.

---

We can approach this problem with either recursion or iteratively with stack to
process the open parentheses.

To do so, we will use the hashmap to count the each elements appeared in the
given formula. We build up the current element whenever upper + lower case is
encountered. When digit is encountered, we build up the number count. When new
upper case character is found, it signals the end of the current element
segment - we record the count of previous element and number count.

If the open parentheses is found, then we need to recurse on itself to find the
count of segement inside the parentheses. Since the individual elements will
get its counts recorded on the recursive call, we just simply have to update
the elements by the digit that is found after the closing braket.

When closing braket is found, we can just add the element to the counter if
found (a single case such as "O") and return the currently built counter and
last index processed.

The time complexity of this problem is O(n * k * log(k)) where k is the length
of the elements that we have to sort in the end. Otherwise, the process of
finding all elements and its count can be done within O(n).

---

Python:

```python
from collections import defaultdict

class Paren:
    OPEN = "("
    CLOSED = ")"

class Solution:
    def countOfAtomsHelper(self, formula, startIndex):
        counter = defaultdict(int)
        elementName = ""
        elementCount = 0
        i = startIndex
        while i < len(formula):
            currentChar = formula[i]
            # if currentChar is uppercase letter
            # it marks the begining of new element segment;
            # record previous elementName: count to Counter
            if currentChar.isupper():
                if elementName:
                    counter[elementName] += elementCount if elementCount else 1
                    elementCount = 0
                elementName = currentChar
            # if lowercase letter,
            # then it extends from current element name (i.e. "Hg")
            elif currentChar.islower():
                elementName += currentChar
            # if it is a digit 0-9,
            # increase the current element's count
                elementCount = (elementCount * 10) + int(currentChar)
            # if it is open paren,
            # recursively extend the segment within the paren,
            # it will return the counter inside the segment and last index til closed paren
            elif currentChar is Paren.OPEN:
                innerCounter, i = counterOfAtomsHelper(formula, i+1)
                parenNum = 0
                while i+1 < len(formula) and formula[i+1].isdigit():
                    parenNum = (parenNum * 10) + int(formula[i+1])
                    i += 1
                # increase element count of returned counts by surrouned paren number
                for n, c in innerCounter.items():
                    counter[n] += c * parenNum if parenNum else 1
i           else:
                if name:
                    counter[name] = elementCount if elementCount else 1
                return (counter, i)
            i += 1
        return (counter, i)

    def countOfAtoms(self, formula):
        formula = "(" + formula + ")"
        counter, _ = countOfAtomsHelper(formula, 0)
        return "".join(
            [name + (str(count) if count > 1 else "") 
                for name, count 
                    in sorted(counter.items())]
        )
```


