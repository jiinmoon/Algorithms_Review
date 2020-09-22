# 528 Random Pick with Weight

class RandomWeight:
    def __init__(self, weights):
        self.weights = list()
        temp = 0
        for weight in weights:
            temp += weight
            self.weights.append(temp)

    def pickRandom(self):
        i = random.randint(1, self.weights[-1])
        return bisect.bisect_left(self.weights, i)
