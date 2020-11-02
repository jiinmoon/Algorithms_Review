# 642 Design Autocomplete System

Design a search autocomplete system for a search engine. Users may input
a sentence (at least one word and end with a special character '#'). For each
character they type except '#', you need to return the top 3 historical hot
sentences that have prefix the same as the part of sentence already typed. Here
are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed
the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is
the hottest one). If several sentences have the same degree of hot, you need to
use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this
case, you need to return an empty list.

---

In order to retrieve the sentences as efficiently as possible for each
character input, we need to maintain a list of sentences that we can matches
with the input upto so far - for this, we need a list to maintain not just the
input, but also the list of matching sentences for the input that we are
building. As well, we also need to record how "hot" or frequency of the
sentences as well since the hotness of the sentences is also required.

Thus, when input is started, we first filter the given sentences that matches
the first character of the input. It is sorted by its frequency. Then, for
subsequent input character, the matching sentences are filtered.

---

Python:

```python

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.inputs = list()
        self.matchs = list()
        self.counter = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.counter[s] = t

    def input(self, char):
        if char == "#":
            # record currently built input string
            self.counter["".join(self.inputs)] += 1
            self.inputs = list()
            self.matchs = list()
            return

        if not self.inputs:
            # we want highest to lowest
            self.matchs = [(-c, s) for s, c in self.counter.items() if s[0] == char]
            self.matchs.sort()
            self.matchs = [s for _, s in self.matchs]
        else:
            i = len(self.inputs)
            self.matchs = [s for s in self.matchs if len(s) > i and s[i] == char]

        self.inputs.append(char)
        return self.matchs[:3]
```

