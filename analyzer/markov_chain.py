import random

class MarkovChain:
    def __init__(self):
        self.trainsitions = dict()

    def add_trainsition(self, v, w):
        if v not in self.trainsitions:
            self.trainsitions[v] = dict()
        if w not in self.trainsitions[v]:
            self.trainsitions[v][w] = 1
        else:
            self.trainsitions[v][w] += 1

    def next(self, v, default=None):
        # TODO: performance can be boosted here, if tree is built
        # print("checking {}".format(v))
        if v not in self.trainsitions:
            if default is not None:
                return default
            else:
                return random.choice(self.tainsisions.keys())
        return random.choices(
            population=list(self.trainsitions[v].keys()), 
            weights=list(self.trainsitions[v].values()))[0]

    def __str__(self):
        output_str = "" 
        for v, w_weights in self.trainsitions.items():
            for w, weight in w_weights.items():
                output_str += "{} -> {} : {}\n".format(v, w, weight)

        return output_str
