""" 109. Convert Sorted List to BST

Question:

    Given a singly linked list where elements are sorted in ascending order,
    convert it to a height balanced BST.

"""

class Solution:
    def sortedLinkedListToBST(self, head):
        if not head or not head.next
            return head

        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at prev to mid node.
        head2 = slow.next
        slow.next = None

        curr = TreeNode(head2.val)
        curr.left = self.sortedLinkedListToBST(head)
        curr.right = self.sortedLinkedListToBST(head2.next)

        return curr
