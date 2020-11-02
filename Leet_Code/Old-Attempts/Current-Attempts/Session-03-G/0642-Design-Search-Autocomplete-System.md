# 642 Design Search Autocomplete System

For each character input, update the list containing the matched sentences so
far.

---

Python:

```python

from collections import defaultdict

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.inputs = list()
        self.matches = list()
        self.d = defaultdict(list)
        for s, t in zip(sentences, times):
            d[s] = t

    def input(self, char):
        if char == "#":
            self.d["".join(self.inputs)] += 1
            self.inputs = list()
            self.matches = list()
            return

        if not self.inputs:
            self.matches = [(-t,s) for s, t in self.d.items() if s[0] == char]
            self.matches.sort()
            self.matches = [s for _, s in self.matches]
        else:
            i = len(self.inputs)
            self.matches = [s for s in self.matches if len(s) > i and s[i] == char]

        self.inputs.append(char)
        return self.matches[:3]
```
