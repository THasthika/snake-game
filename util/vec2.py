import math


class Vec2:

    x = 0
    y = 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x + other, self.y + other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x + other.x, self.y + other.y)

        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x - other, self.y - other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x - other.x, self.y - other.y)

        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x * other, self.y * other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x * other.x, self.y * other.y)

        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x / other, self.y / other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x / other.x, self.y / other.y)

        raise TypeError()

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x // other, self.y // other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x // other.x, self.y // other.y)

        raise TypeError()

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def distance(self, other):
        return self.distanceL2(other)

    def distanceL2(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distanceL1(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def unit_vector(self):
        return self / self.magnitude()

    def __repr__(self) -> str:
        return "Vec2({}, {})".format(self.x, self.y)

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def __iter__(self):
        for x in (self.x, self.y):
            yield x
