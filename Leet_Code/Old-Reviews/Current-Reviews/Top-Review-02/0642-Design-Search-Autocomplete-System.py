# 642 Design Search Autocomplete System

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.inputs = list()
        self.matches = list()
        self.counts = collections.defaultdict(int)
        for s, t in zip(sentences, times):
            self.counts[s] = t

    def input(self, char):
        if char == "#":
            self.counts["".join(self.inputs)] += 1
            self.inputs = list()
            self.matches = list()
            return
        elif not self.inputs:
            self.matches = [(-t,s) for s, t in self.counts if s[0] == char]
            self.matches.sort()
            self.matches = [s for _, s in self.matches]
        else:
            i = len(self.inputs)
            self.matches = [s for s in self.matches if len(s) > i and s[i] == char]
        self.inputs.append(char)
        return self.matches[:3]
