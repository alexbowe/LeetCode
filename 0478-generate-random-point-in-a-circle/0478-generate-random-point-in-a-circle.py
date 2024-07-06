from dataclasses import dataclass

@dataclass
class Range:
    lo: float
    hi: float

    def random(self):
        return random.uniform(self.lo, self.hi)

@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        dx = self.x-other.x
        dy = self.y-other.y
        return (dx*dx+dy*dy)**0.5
    
    def __iter__(self):
        yield self.x
        yield self.y

@dataclass
class Rectangle:
    x_range: Range
    y_range: Range

    def random(self):
        x = self.x_range.random()
        y = self.y_range.random()
        return Point(x,y)

@dataclass
class Circle:
    center: Point
    radius: float

    def bounding_box(self):
        return Rectangle(
            Range(
                self.center.x - self.radius,
                self.center.x + self.radius
            ),
            Range(
                self.center.y - self.radius,
                self.center.y + self.radius,
            ),
        )

    def __contains__(self, pt):
        return self.center.distance(pt) <= self.radius
    
    def random(self):
        box = self.bounding_box()
        pt = box.random()
        while pt not in self:
            pt = box.random()
        return pt
    
    def random_fast(self):
        theta = random.uniform(0, 2*math.pi)
        R = self.radius*(random.uniform(0,1))**0.5
        return Point(
            self.center.x + R*math.cos(theta),
            self.center.y + R*math.sin(theta),
        )

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self._circle = Circle(Point(x_center, y_center), radius)

    def randPoint(self) -> List[float]:
        return [*self._circle.random_fast()]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()