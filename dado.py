import numpy as np


class Dado:

    lados: int
    nivel_pifia: int
    nivel_abierta: int

    def roll(self):
        return np.random.randint(1, 1 + self.lados)

    def __init__(self, sides):
        self.lados = sides
