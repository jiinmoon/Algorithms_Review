# 118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's
triangle.

---

Python:

```python

class Solution118:

    def generate(self, numRows: int) -> List[List[int]]:
        
        if not numRows:
            return []
        
        result = [[1] , [1, 1]]
        
        if numRows < 2:
            return result[:numRows]
        
        for _ in range(2, numRows):
            m = len(result[-1])
            temp = [1] * (m + 1)
            for i in range(m-1):
                temp[i+1] = result[-1][i] + result[-1][i+1]
            result.append(temp)

        return result
```
