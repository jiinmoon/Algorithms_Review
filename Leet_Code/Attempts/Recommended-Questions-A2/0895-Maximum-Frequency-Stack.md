# 895. Maximum Frequency Stack

Implement FreqStack, a class which simulates the operation of a stack-like data
structure.

FreqStack has two functions:

```
push(int x), which pushes an integer x onto the stack.

pop(), which removes and returns the most frequent element in the stack.

If there is a tie for most frequent element, the element closest to the top of
the stack is removed and returned.
```
---

We can support these operations in O(1) by having a list of stacks - where
index of the list denotes the frequency of the values. As new values are added,
we push them unto their respective stacks indicated by its current frequency
(i.e. if the current count of value is 3, then it pushes unto stack located at
index 2).

As we add them, we create a new stack to add if the frequency increases.
Likewise, we remove any empty stacks if last element has been removed.

---

```java

class Solution895 {
    
    private Map<Integer, Integer> counter;
    private List<Stack<Integer>> stacks;

    public Solution895()
    {
        this.counter = new HashMap<>();
        this.stacks = new ArrayList<>();
    }

    public void push(int value)
    {
        this.counter.put(value, this.counter.getOrDefault(value, 0) + 1);
        // new stack is required to match the new count
        if (this.counter.get(value) > this.stacks.size())
            this.stacks.add(new Stack<>();
        // add to last stack indicated by the count
        this.stacks.get(this.counter.get(value) - 1).push(value);
    }

    public int pop()
    {
        int val = this.stacks.get(this.stacks.size()-1).pop();
        this.counter.put(val, this.counter.get(val) - 1);

        // remove empty stack
        if (this.stacks.get(this.stacks.size()-1).isEmpty())
            this.stacks.remove(this.stacks.size()-1);

        return val;
    }
}

```
