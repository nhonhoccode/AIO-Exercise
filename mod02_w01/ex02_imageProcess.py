import matplotlib.image as mpimg
import numpy as np


# Question 12, 13, 14


def to_gray(img, method):
    h, w, _ = img.shape
    gray_img = np.ones((h, w))
    for height in range(h):
        for width in range(w):
            R, G, B = img[height][width]
            if method == "Lightness":
                gray_img[height][width] = (max(R, G, B) + min(R, G, B)) / 2
            elif method == "Average":
                gray_img[height][width] = sum([R, G, B]) / 3
            elif method == "Luminosity":
                gray_img[height][width] = 0.21 * R + 0.72 * G + 0.07 * B
    return gray_img


img = mpimg.imread("dog.jpeg")
gray_img_01 = to_gray(img, method="Lightness")
print("12A.", gray_img_01[0, 0], sep="\n")
gray_img_02 = to_gray(img, method="Average")
print("13A.", gray_img_02[0][0], sep="\n")
gray_img_03 = to_gray(img, method="Luminosity")
print("14C.", gray_img_03[0][0], sep="\n")