733 Flood Fill
==============

An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image.

Given a coordinate (sr, sc) representing the starting pixel of the flood fill,
and a pxiel value newColor, "flood fill" the image.

To perform it, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels. REplace the color of
all of the aforementioned pixels with the newColor.

---

We will simply expand from the given point, and replace the the state as long
as it matches wtth the original color that it was selected with.

---

Python: Recursive approach.

```python
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        m, n = len(image), len(image[0])
        target = image[sr][sc] 
        
        def fill(r, c):
            if image[r][c] != target:
                return
            image[r][c] = newColor
            for nR, nC in [ (r+1, c), (r-1, c), (r, c+1), (r, c-1) ]:
                if nR >= 0 and nR < m and nC >= 0 and nC < n:
                    fill(nR, nC)

        fill(sr, sc)
        return image
```

Go: Iterative DFS approach.

```go
func floodFill(image [][]int, sr, sc, newColor int) [][]int {
    if image[sr][sc] == newColor { return image }

    var (
        oColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        stk = [][]int{ []int{sr, sc} }
        cur = []int{}
    )

    for len(stk) != 0 {
        cur, stk = stk[len(stk)-1], stk[:len(stk)-1]
        r, c := cur[0], cur[1]
        if r < 0 || r >= m || c < 0 || c >= n { continue }
        if image[r][c] != oColor { continue }
        image[r][c] = newColor
        stk = append(stk, []int{ r+1, c })
        stk = append(stk, []int{ r-1, c })
        stk = append(stk, []int{ r, c+1 })
        stk = append(stk, []int{ r, c-1 })
    }
    return image
}
```
