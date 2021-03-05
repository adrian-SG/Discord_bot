import numpy as np


class Dado:

    lados: int

    def roll(self):
        return np.random.randint(1, 1 + self.lados)

    def __init__(self, sides):
        self.lados = sides
