from pygame import Rect

class GameObject:
    def __init__(self, x, y, width, height, speed=(0,0)):
        self.bounds = Rect(x, y, width, height)
        self.speed = speed

    @property
    def top(self):
        return self.bounds.top
    @property
    def left(self):
        return self.bounds.left
    @property
    def bottom(self):
        return self.bounds.bottom
    @property
    def right(self):
        return self.bounds.right
    @property
    def width(self):
        return self.bounds.width
    @property
    def height(self):
        return self.boundes.height

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        self.bounds.move(dx, dy)

    def update(self):
        if self.speed == (0,0):
            return
        self.move(*self.speed);
