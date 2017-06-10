import numpy as np

class Coin:
    def __init__(self):
        self.__r = np.random.randint(1)
    def __call__(self, N):
        return sum([i <= self.r for i in np.random.rand(N, 1)])
    @property
    def r(self):
        return self.__r
