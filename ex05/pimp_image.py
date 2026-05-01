import cv2
import numpy as np
from load_image import ft_load


def ft_invert(mat: np.ndarray) -> np.ndarray:
    def _invert(x: np.uint8) -> np.uint8:
        return 255 - x

    ufn_invert = np.vectorize(_invert)
    return ufn_invert(mat)


def ft_red(mat: np.ndarray) -> np.ndarray:
    mat[:, :, 0] = 0
    mat[:, :, 1] = 0
    return mat


def ft_green(mat: np.ndarray) -> np.ndarray:
    mat[:, :, 0] = 0
    mat[:, :, 2] = 0
    return mat


def ft_blue(mat: np.ndarray) -> np.ndarray:
    mat[:, :, 1] = 0
    mat[:, :, 2] = 0
    return mat


def ft_grey(mat: np.ndarray) -> np.ndarray:
    grey = np.dot(mat[..., ::-1], [0.299, 0.587, 0.114]).astype(np.uint8)
    return grey


im = ft_load("landscape.jpg")
im = ft_grey(im)

cv2.imshow("Test", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
