import cv2
import numpy as np
class geometrikSekiller:
    def __init__(self, width, height):
        self.image = np.zeros((height, width, 3), dtype = "uint8")
        self.top_left = None
        self.bottom_right = None
        self.color = None
        self.corners = None
        self.center = None
        self.radius = None
    def kare(self):
        top_left = (50, 50)
        bottom_right = (200, 200)
        color = (255, 0, 0)
        cv2.rectangle(self.image, top_left, bottom_right, color, 2)
    def ucgen(self):
        corners = np.array([[350, 50], [250, 200], [450, 200]], np.int32)
        corners = corners.reshape((-1, 1, 2))
        color = (0, 255, 0)
        cv2.polylines(self.image, [corners], isClosed=True, color=color, thickness=2)
    def dikdortgen(self):
        top_left = (500, 50)
        bottom_right = (750, 200)
        color = (0, 0, 255)
        cv2.rectangle(self.image, top_left, bottom_right, color, 2)
    def daire(self):
        center = (450, 350)
        radius = 75
        color = (255, 0, 255)
        cv2.circle(self.image, center, radius, color, 2)
    def img_show(self, window_name="resim-ciktisi"):
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

width, height = 800, 800
output = geometrikSekiller(width, height)
output.kare()
output.ucgen()
output.dikdortgen()
output.daire()
output.img_show()










