23 Merge k Sorted Lists
=======================

Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.

---

Absolute brute force approach would be to grab all the values, sort them, and
construct a new linked list. O(n * log(n)) time complexity is required - O(n)
to retrieve all values, O(n * log(n)) to sort, and O(n) to construct new list.

Naive approach would be to consider every first node from each of the k lists
and append them to the new list. Since there are k lists, this would be O(k
* n) time complexity algorithm where k is the number of lists and n is the
  longest linked list in given list.

The better approach would be to realize that we can use the divide and conquer
approach here. We take two lists, merge them, and place it back into the fold.
Since we are reducing the number of lists by half each time, the algorithm can
complete in O(n * log(k)) time.

---

Go:

```go
func mergeKLists(lists []*ListNode) *ListNode {
    if lists == nil || len(lists) == 0 {
        return nil
    }
    for ; len(lists) > 1; lists = lists[2:] {
        l1, l2 := lists[0], lists[1]
        lists = append(lists, mergeTwoLists(l1, l2))
    }
    return lists[0]
}

func mergeTwoLists(l1, l2 *ListNode) *ListNode {
    if l1 == nil { return l2 }
    if l2 == nil { return l1 }
    if l1.Val < l2.Val {
        l1.Next = mergeTwoLists(l1.Next, l2)
    } else {
        l2.Next = mergeTwoLists(l1, l2.Next)
    }
}
```

