import math
      
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self,index):
        return self.coordinates[index]

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        result = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(result)
    
    def __sub__(self, v):
        result = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(result)
    
    def __mul__(self, v):
        if isinstance(v, Vector):
            result = [x*y for x, y in zip(self.coordinates, v.coordinates)]
            return sum(result)
        else:
            return Vector([x*v for x in self.coordinates])

    def norm(self):
        result = [x*x for x in self.coordinates]
        result = sum(result)
        return math.sqrt(result)

    def unit(self):
        return self * self.norm()

    def angle(self, v):
        dotValue = self * v
        norm1 = self.norm()
        norm2 = v.norm()
        return math.acos(dotValue / (norm1*norm2))

    def proj(self, v):
        v = v * (1.0 / v.norm())
        return v * (v * self)

    def is_parallel(self, v):
        if v == Vector([0] * v.dimension):
            return True
        else:
            items = [x / y for x, y in zip(self.coordinates, v.coordinates)]
            return all([abs(items[0] - item) < 1e-10 for item in items])

    def is_orthogonal(self, v):
return abs(self * v) < 1e-10
