155 Min Stack
=============

Implement a stack that supports typical stack operations as well as `min()`
that retrieves the minimum of the stack in O(1).

---

In order to support the min operation in constant time, we simply maintain
a separate stack that only maintains the current minimum. Whenever we push an
item onto the stack, we check whether top of minStack is greater, in which case
the new item is the current minimum. And when we pop, we also check against top
of the minStack to update the current minimum.

---

C++:

```cpp

using std::stack;

class MinStack {

public:
    stack<int> minStk;
    stack<int> stk;

    MinStack() {}

    void push(int x) {
        if (this->minStk.empty() || this->minStk.top() >= x)
            this->minStk.push(x);
        this->stk.push(x);
    }

    void pop() {
        if (!this->minStk.empty() && this->minStk.top() == this->stk.top())
            this->minStk.pop();
        this->stk.pop();
    }

    int top() { return this->stk.top(); }

    int getMin() { return this->minStk.top(); }

};
```

