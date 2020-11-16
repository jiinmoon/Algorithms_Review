# 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

---

One approach would be to use linear algebra - perform matrix transformation
involving sin(). This would be undesirable as it would require matrix
multiplication which would cost us O(n^3) in time complexity in worst case.

Other methods could involve various manipulation of pointers to rotate the
image. But simplest trick here is to first reverse the given matrix row-wise.
Then, we can simply perform swap for values across diagnoal line. This would be
O(n^2) in time complexity.

---

Python:

```python

class Solution:
    def rotateImage(self, image):
        if not image:
            return

        image.reverse()
        for i in range(len(image)):
            for j in range(i, len(image)):
                image[i][j], image[j][i] = image[j][i], image[i][j]
```
