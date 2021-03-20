import cv2
import math

class Kanada:
    def __init__(self, x0, y0, color=(90, 250, 255)):
        self.color = color
        self.x0 = x0
        self.y0 = y0
    def circle(self, frame, size, coords):
        # outer lightning
        overlay = frame.copy()
        s = size + 3
        for i in range(2):
            cv2.circle(overlay, coords, s, self.color, thickness=1, lineType=cv2.LINE_AA)
            frame = cv2.addWeighted(overlay, 0.3, frame, 1 - 0.3, 0)
            s += 1
        # in
        alpha = 0.07
        overlay = frame.copy()
        s = size
        for i in range(math.floor(size/2)):
            cv2.circle(overlay, coords, s, self.color, thickness=3, lineType=cv2.LINE_AA)
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
            s -= 2
            alpha = max(0, alpha-0.0026)
        return frame
    def line(self, frame, size, a, coords1, coords2):
        alpha = a
        overlay = frame.copy()
        for i in range(1, size):
            cv2.line(overlay, coords1, coords2, self.color, thickness=i)
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
            alpha -= a/size
        return frame
