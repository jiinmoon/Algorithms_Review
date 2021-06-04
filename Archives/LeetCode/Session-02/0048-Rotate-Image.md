# 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

---

There are several approaches that we can try to rotate an image.

One possible solution would be to compute the correct coordinates for each
position (i, j) to swap the values along. Another solution would be to use the
matrix transformation from linear algebra but this would involve matrix
multiplication involving trigs.

One trick that we can use to solve this problem in linear time would be to
first, transform the given matrix upside down. Then, we swap the values across
the diagonal line.

---

Python:

```python

class Solution48:

    def rotateImage(self, image):

        image.reverse()

        for i in range(1, len(image)):
            for j in range(i, len(image)):
                image[i][j], image[j][i] = image[j][i], image[i][j]
```
