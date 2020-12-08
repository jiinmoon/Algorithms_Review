# 1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The
robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the
robot never leaves the circle.

---

There is a trick where if there is a cycle, repeating the same instructions
4 times will place us back at the start. Hence, we simulate the instructions
4 times to check whether we have returned to original position. Time complexity
would be O(n).

---

Python:

```python

class Solution1041:

    def __init__(self):
        self.directions = {
            "N" : (0, 1),
            "E" : (1, 0),
            "S" : (0, -1),
            "W" : (-1, 0)
        }

        self.facings = {
            "L" : {
                "N": "W",
                "E": "N",
                "S": "E",
                "W": "S"
            },
            
            "R" : {
                "N" : "E",
                "E" : "S",
                "S" : "W",
                "W" : "N"
            }
        }


    def isRobotBounded(self, instructions: str) -> bool:

        x, y, face = 0, 0, "N"
        
        for i in instructions * 4:

            if i == "G":
                dx, dy = self.directions[face]
                x += dx
                y += dy

            else:
                face = self.facings[i][face]

        return x == y == 0
```
