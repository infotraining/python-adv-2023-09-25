import math
import pytest
from dataclasses import dataclass
import dataclasses

@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    # def __init__(self, x: float, y: float):
    #     self.x = x
    #     self.y = y

    # def __eq__(self, other: 'Vector') -> bool:
    #     return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)
    
    def __mul__(self, other: float) -> 'Vector':
        return Vector(self.x * other, self.y * other)

    def __bool__(self):
        return bool(self.x or self.y)

    # def __repr__(self):
    #     return f"Vector(x={self.x!r}, y={self.y!r})"
    
    def __str__(self):
        return f"Vector with coordinates: (x={self.x}, y={self.y})"

    @property
    def angle(self) -> float:
        return math.atan2(self.y, self.x)
    
    # def __hash__(self):
    #     return hash((self.x, self.y))
    
    def __iter__(self):
        return iter((self.x, self.y))


def test_Vector_init():
    v = Vector(1, 2)
    assert v.x == 1
    assert v.y == 2


def test_Vector_addition():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    assert v1 + v2 == Vector(4, 5)


def test_Vector_abs():
    v = Vector(3, 4)
    assert abs(v) == 5.0


def test_Vector_multiplication():
    v = Vector(3, 4)
    assert v * 3 == Vector(9, 12)


def test_Vector_conversion_to_bool():
    v = Vector(0, 0)
    assert not v

    v = Vector(1.0, 0.0)
    assert v


def test_Vector_repr():
    v = Vector(1, 2)
    v_clone = eval(repr(v))
    assert v == v_clone


def test_Vector_iterator():
    import pytest
    v = Vector(3, 4)

    it = iter(v)
    assert next(it) == 3
    assert next(it) == 4

    with pytest.raises(StopIteration):
        next(it)


@pytest.mark.parametrize("x,y,angle", [
    (0.0, 0.0, 0.0),
    (1.0, 0.0, 0.0),
    (0.0, 1.0, math.pi/2),
    (1.0, 1.0, math.pi/4)
])
def test_Vector_angle(x, y, angle):
    v = Vector(x, y)
    assert v.angle == pytest.approx(angle, 0.0001)


def test_Vector_hashing():
    v1 = Vector(6.5, 7.0)
    v2 = Vector(6.5, 7.0)

    assert v1 == v2
    assert hash(v1) == hash(v2)
