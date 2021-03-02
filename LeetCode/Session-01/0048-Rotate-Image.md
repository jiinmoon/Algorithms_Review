# 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

---

Naive approach would be to compute the rotated coordinates and iterate to move
all the values. Another approach involves linear algebra and matrix
transformation - but this requires a matrix multiplication which is O(n^3) in
naive implementation with possible improvement.

Best approach involves a trick: we can rotate the image by first reversing the
rows, then swap the elements across the diagonal line. Hence, we can perform
this rotation in O(n) time.

---

Python:

```python

class Solution48:

    def rotateImage(self, image):

        image.reverse()

        for i in range(len(image)):
            for j in range(len(image[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
