# 1628. Design an Expression Tree With Evaluate Function

Given the postfix tokens of an arithmetic expression, build and return the
binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the
operands (numbers) appear before their operators. For example, the postfix
tokens of the expression 4*(5-(7+2)) are represented in the array postfix
= ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary
expression tree. The returned tree will be tested using the evaluate function,
which is supposed to evaluate the tree's value. You should not remove the Node
class; however, you can modify it as you wish, and you can define other classes
to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic
expressions. Each node of a binary expression tree has either zero or two
children. Leaf nodes (nodes with 0 children) correspond to operands (numbers),
and internal nodes (nodes with two children) correspond to the operators '+'
(addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute
value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular?
For example, is your design able to support additional operators without making
changes to your existing evaluate implementation?

---

Postfix expression can be simply computed with a stack data structure and its
LIFO operation. Similarly, our tree will share that trait with the recursion.

Here, we note that we have two different types of nodes - Operators node and
Nums node. The numbers will always appear at the leaf whereas operators are
discovered along the path.

Using stack, we can build our expression as we iterate on the given expression
as follows:

(1) if current char is an operator, then it becomes a new operator whose childs
are previous two nodes on top of our stack.

(2) if current char is a num, then it becomes a new num node to be added onto
top of stack.

Then, evaluation is simple: operators node has its value as a value of
operator; which should be performed to its left and right subtree's evaluted
values. And nums node will simply return their values as is.

---

Python:

```python

import abc
from abc import ABC, abstractmethod

class Node(ABC):

    @abstractmethod
    def evaluate(self):
        pass


class NumNode(Node):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left, self.right = left, right
    
    def evaluate(self):
        return self.value


class OpNode(Node):
    
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left, self.right = left, right

    def evaluate(self):
        l, r = self.left.evaluate(), self.right.evaluate()

        if self.value == "+":
            return l + r
        elif self.value == "-":
            return l - r
        elif self.value == "*":
            return l * r
        elif self.value == "/":
            return l // r


class TreeBuilder(object):

    def buildTree(self, postfix):

        stack = list()

        for s in postfix:
            # is operator
            if s in {"+", "-", "*", "/"}:
                curr = OpNode(value = s)
                curr.right = stack.pop()
                curr.left = stack.pop()
                stack.append(curr)
            else:
                stack.append(NumNode(value = int(s)))

        return stack[-1] if stack else None

```
