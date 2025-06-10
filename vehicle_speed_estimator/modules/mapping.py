import cv2 as cv
import numpy as np

class Cam2WorldMapper:
    def __init__(self):
        self.M = None

    def find_perspective_transform(self, image_pts, world_pts):
        image_pts = np.asarray(image_pts, dtype=np.float32).reshape(-1, 1, 2)
        world_pts = np.asarray(world_pts, dtype=np.float32).reshape(-1, 1, 2)
        self.M = cv.getPerspectiveTransform(image_pts, world_pts)
        return self.M

    def map(self, image_pts):
        if self.M is None:
            raise ValueError("Perspective transform not set.")
        image_pts = np.asarray(image_pts, dtype=np.float32).reshape(-1, 1, 2)
        return cv.perspectiveTransform(image_pts, self.M).reshape(-1, 2)
