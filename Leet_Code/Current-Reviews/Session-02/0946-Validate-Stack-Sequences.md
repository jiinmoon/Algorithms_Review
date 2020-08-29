946 Validate Stack Sequences
============================

Given two sequences pushed and popped with distinct values, return true if and
only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

---

Simply, we maintain a stack. For every value in the pushed, we first push unto
the stack. Then, while the top of the stack matches the top of the popped, we
pop from both our stack and the popped. If we do not have any elements left
over in popped, we have our valid stack sequence.

---

C++:

```cpp

class Solution {
public:
    bool isValidStkSequences(vector<int>& pushed, vector<int>& popped) {
        vector<int> stk;
        int i = 0;
        for (auto num : pushed) {
            stk.push_back(num);
            for (; stk.size() > 0 && stk.back() == popped[i]; ++i, stk.erase(stk.end()-1));
        }
        return i == popped.size();
    }
}
```

