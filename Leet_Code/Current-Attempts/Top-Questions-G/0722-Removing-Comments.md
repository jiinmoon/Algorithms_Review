# 722 Removing Comments

Given a C++ program, remove comments from it. The program source is an array
where source[i] is the i-th line of the source code. This represents the result
of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the
characters to the right of it in the same line should be ignored.

The string /\* denotes a block comment, which represents that all characters
until the next (non-overlapping) occurrence of \*/ should be ignored. (Here,
occurrences happen in reading order: line by line from left to right.) To be
clear, the string /\*/ does not yet end the block comment, as the ending would
be overlapping the beginning.

The first effective comment takes precedence over others: if the string //
occurs in a block comment, it is ignored. Similarly, if the string /\* occurs in
a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output
that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.
For example, source = "string s = "/\* Not a comment. \*/";" will not be a test
case. (Also, nothing else such as defines or macros will interfere with the
comments.)

It is guaranteed that every open block comment will eventually be closed, so /\*
outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please
see the examples below for details.

After removing the comments from the source code, return the source code in the
same format.

---

Removing comments require analyzing the given source doe line by line - and go
through them in every two characters to analyze the cases. If it is comment, we
need to mark it as so and add to the source code.

---

Python:

```python

class Solution:
    def removeComments(self, source):
        result, temp = list(), list()
        isComment = False

        for line in source:
            i = 0
            while i < len(line):
                curr = line[i:i+2]
                if not isComment and curr == '\*':
                    isComment = True
                    i += 2
                elif not isComment and curr == '//':
                    i = len(line)
                elif isComment and curr == '*/':
                    isComment = False
                    i += 2
                elif isComment:
                    i += 1
                else:
                    temp.append(line[i])
                    i += 1

            if temp and not isComment:
                result.append("".join(temp))
                temp = list()

        if temp:
            result.append("".join(temp))

        return result
```
