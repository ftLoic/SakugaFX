from sakugafx.kanada import *
import os
import cv2
import numpy as np

if not os.path.isdir('output'):
    os.mkdir('output')

frame = np.zeros((720, 1280, 3), np.uint8)
frame[:] = (80, 30, 5)
kanada = Kanada(500, 500, (255, 255, 255))

frame = kanada.line(frame, 20, 0.2, (-10, -50), (900, 860))
frame = kanada.line(frame, 20, 0.2, (410, -10), (0, 400))

frame = kanada.circle(frame, 100, (200, 200))
frame = kanada.circle(frame, 80, (300, 300))
frame = kanada.circle(frame, 30, (480, 460))
frame = kanada.circle(frame, 60, (660, 640))

cv2.imwrite("output/kanada.jpg", frame)

cv2.imshow("Kanada Light Flare", frame)
cv2.waitKey()