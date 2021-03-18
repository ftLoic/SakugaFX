import cv2
import random

class Kutsuna:
    def __init__(self, x0, y0, dx, dy, start=0, lifespan=24, color=(0, 0, 255), size=20):
        self.color = color
        self.start = start
        self.x0 = x0
        self.y0 = y0
        self.dx = dx
        self.dy = dy
        self.lifespan = lifespan+start
        self.size = size
    def translateX(self, v):
        for i in range(len(self.dx)):
            self.dx[i] += v
    def translateY(self, v):
        for i in range(len(self.dy)):
            self.dy[i] += v
    def write(self, frame, nframe):
        x = self.x0
        y = self.y0
        # Random size
        size = self.size+random.randint(-10,10)
        # Kind of ease-in/ease-out
        end = self.lifespan-nframe
        if nframe < 4:
            size = round(size/(4-nframe))
        if end < 4:
            size = round(size/(4-end))
        if end < 0 or nframe < self.start:
            return
        size = max(15, size)

        # Draw the circles randomly
        height, width, channels = frame.shape
        for f in range(width):
            x += round(random.choice(self.dx))
            y += round(random.choice(self.dy))
            cv2.circle(frame, (x, y), size, self.color, thickness=-1, lineType=8)