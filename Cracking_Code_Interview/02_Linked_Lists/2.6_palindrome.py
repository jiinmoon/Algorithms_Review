""" 2.6 Palindrome

Question:

    Implement a function to check if a linked list is a palindrome.

---

There are various ways to accomplishing this task but the efficient way is to
reverse the half of the list that is either first half or last half, then
compare whether the numbers are equal.

This is particularly easier if we use Stack structure to store the first half of
the elements to compare the later half. This is accomplished by preparing two
pointers which move at different 'speed' - that is one moves twice as fast such
that the pointer lagging behind will be a middle of the list when the faster one
has reached the end.

The challenge is in detecting the odd or even number of list. If it is even, we
do not have to care, but when it is odd, we will have to skip the number once
more.

"""

class Solution:

    def isPalindrome(self, head):
        if not head: return False
        stack = list()
        slow, fast = head
        while fast and fast.next:
            stack.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()
            if slow.val != top: return False
            slow = slow.next

        return True

