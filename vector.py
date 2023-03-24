import math
class Vector:
    def __init__(self, a):
       self._coords = a[:]
       self._n = len(a)
    def __add__(self, other):
        result = [0 for i in range(self.n)]
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return result
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    def scale(self, alpha):
        result = []
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

    def direction(self): return self.scale(1.0 / abs(self))

    def __getitem__(self, i): return self._coords[i]
    def __abs__(self): return math.sqrt(self.dot(self))
    def __len__(self): return self._n
    def __str__(self): return str(self._coords)

