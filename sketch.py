from vector import Vector

class Sketch:
    def __init__(self, text, k, d):
        freq = [0 for i in range(d)]
        for i in range(len(text) - k):
            kgram = text[i:i+k]
            freq[hash(kgram) % d] += 1
        vector = Vector(freq)
        self._sketch = vector.direction()
    def similarTo(self, other):
        return self._sketch.dot(other._sketch)

    def __str__(self):
        return str(self._sketch)
