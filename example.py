from kutsunagen.kutsunagen import Kutsuna
import os
import cv2
import numpy as np

k1 = Kutsuna(x0=0, y0=0, dx=[-7,2,5,7], dy=[-7,2,5,7], start=0, lifespan=26, color=(255, 40, 255), size=30)
k2 = Kutsuna(x0=1920, y0=0, dx=[-7,2,5,7], dy=[-7,2,5,7], start=0, lifespan=40, color=(255, 40, 40), size=26)
k3 = Kutsuna(x0=1920, y0=900, dx=[-5,-2,2,5], dy=[-8,-5,2,5], start=0, lifespan=50, color=(255, 255, 40), size=18)
for i in range(64):
    frame = np.zeros((1080, 1920, 3), np.uint8)
    frame.fill(255)

    k1.write(frame, i)
    k2.write(frame, i)
    k3.write(frame, i)
    k1.translateX(0.2)
    k2.translateX(-0.2)
    k3.translateX(-0.5)

    cv2.imwrite("frame%02d.jpg" % (i,), frame)
# os.system("ffmpeg -i frame%02d.jpg -c:v libx264 -vf fps=24 -pix_fmt yuv420p -preset slow -crf 20 -s 1280x720 -y out.mp4")