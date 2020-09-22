# 160 Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, a, b):
        if not (a and b):
            return a or b

        currA, currB = a, b
        while currA != currB:
            currA = b if not currA else currA.next
            currB = a if not currB else currB.next

        return currA
