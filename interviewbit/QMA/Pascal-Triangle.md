# Pascal Triangle

Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

---

Python:

```python

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        
        if not A:
            return []
        
        result = [[1], [1,1]]
        
        if A < 2:
            return result[:A]
        
        for _ in range(2, A):
            m = len(result[-1])
            temp = [1] * (m + 1)
            for i in range(m-1):
                temp[i+1] = result[-1][i] + result[-1][i+1]
            result.append(temp)
            
        return result

```
