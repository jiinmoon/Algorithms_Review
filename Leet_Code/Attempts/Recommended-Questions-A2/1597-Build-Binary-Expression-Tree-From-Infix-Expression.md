# 1597. Build Binary Tree Expression Tree From Infix Expression

A binary expression tree is a kind of binary tree used to represent arithmetic
expressions. Each node of a binary expression tree has either zero or two
children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
and internal nodes (nodes with 2 children) correspond to the operators '+'
(addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents
is (A o B), where A is the expression the left subtree represents and B is the
expression the right subtree represents.

You are given a string s, an infix expression containing operands, the
operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal
reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in
parentheses are evaluated first, and multiplication and division happen before
addition and subtraction.

Operands must also appear in the same order in both s and the in-order
traversal of the tree.

---

We use two stacks to maintain our current list of nodes as well as the
operators that we encounter. There are several cases as we iterate on the given
expression:

(1) Given char is a digit. In this case, this forms a single Node that we can
push unto our list of nodes.

(2) Given char is a operator. And here are possibilities:

(2-1) If the operator is + or -, then we also check for our operators that we
have examined so far and see that top of our operator stack is also one of
operators +, -, *, or /. this forms a case where current node is the given
operator char, and left and right nodes are determined by the two most recent
nodes added unto our list of nodes built. Hence, we create a new node when
operator as its value and fix the left and right nodes.

(2-2) If the operator is * or /, we should also check for top of our operators
stack for matching operator for precendence. If it is, we can create a new node
and fix left and right pointers from top of our list of nodes.

(3) Given operator is either open or closed parentheses. If it is open, we add
unto operators stack so that when we encounter closed parentheses, we know how
far we have to loop back as we build our nodes.

After all these operations, we have a list of nodes in order; now, we can
simply repeat the process of building the tree.

Take an example of an expression "2-3/(5*2)+1":

```

1. char is 2; it creates a new node of 2.

2. char is "-"; as operator stack is empty, we simply push.

3. char is 3; it create a new node of 3.

4. char is "/"; it is a new operator and top of our operator is not empty; this
   indicates that there is a previous expression needs to be built. we create
   a new node of "-" and fix its left as 2 and right as 3.

5. char is "("; it will be used as a guard for next ")" encountered. Push it unto
   our operator stack.

6. char is 5; it creates a new node of 5;

7. char is "*"; top of our operator stack is "(" which indicates that no nodes
   are created for now, but to be evaluated later after inner parentheses are
   collapsed.

8. char is ")"; until matching "(" is found, we continously fix our expression
   within the resulting nodes.

9. ...

```

---

Python:

```python

class Solution:

    def expTree(self, s):

        def build():
            operator, right, left = seenThusFar.pop(), digits.pop(), digits.pop()
            result.append(Node(operator, left, right))

        seenThusFar, result = list(), list()

        for char in s:
            if char.isdigit():
                result.append(Node(char, None, None))
            elif char in {"+", "-", "*", "/"}:
                if seenThusFar and seenThusFar[-1] in {"+", "-", "*", "/"}:
                    build()
                seenThusFar.append(char)
            elif char == "(":
                seenThusFar.append(char)
            elif char == "0":
                while seenThusFar and seenThusFar[-1] != ")":
                    build()
                seenThusFar.pop() # remove matching "("
        
        while seenThusFar:
            build()

        return result[0]
```
