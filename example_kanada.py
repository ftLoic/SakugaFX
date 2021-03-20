from sakugafx.kanada import *
import os
import cv2
import numpy as np

if not os.path.isdir('output'):
    os.mkdir('output')

frame = np.zeros((720, 1280, 3), np.uint8)
frame[:] = (80, 30, 5)

# White
kanada = Kanada(500, 500, (255, 255, 255))

frame = kanada.line(frame, 20, 0.2, (-10, -50), (900, 860))
frame = kanada.line(frame, 20, 0.2, (410, -10), (0, 400))

frame = kanada.circle(frame, 100, 0.07, 0.0026, (200, 200))
frame = kanada.circle(frame, 80, 0.07, 0.0026, (300, 300))
frame = kanada.circle(frame, 30, 0.07, 0.0026, (480, 460))
frame = kanada.circle(frame, 60, 0.07, 0.0026, (660, 640))

# Yellow
kanada = Kanada(500, 500, (110, 255, 245))

frame = kanada.line(frame, 30, 0.1, (100, -50), (1400, 640))
frame = kanada.line(frame, 30, 0.1, (900, -10), (-10, 600))

frame = kanada.circle(frame, 180, 0.04, 0.001, (500, 200))
frame = kanada.circle(frame, 130, 0.04, 0.001, (300, 360))

cv2.imwrite("output/kanada.jpg", frame)

cv2.imshow("Kanada Light Flare", frame)
cv2.waitKey()