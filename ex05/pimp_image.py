import numpy as np


def ft_invert(mat: np.ndarray) -> np.ndarray:
    """Invert the values of every pixels in an image"""

    def _invert(x: np.uint8) -> np.uint8:
        return 255 - x

    ufn_invert = np.vectorize(_invert)
    return ufn_invert(mat)


def ft_red(mat: np.ndarray) -> np.ndarray:
    """Mute all color channel of an image except for red"""
    mat[:, :, 0] = 0
    mat[:, :, 1] = 0
    return mat


def ft_green(mat: np.ndarray) -> np.ndarray:
    """Mute all color channel of an image except for green"""
    mat[:, :, 0] = 0
    mat[:, :, 2] = 0
    return mat


def ft_blue(mat: np.ndarray) -> np.ndarray:
    """Mute all color channel of an image except for blue"""
    mat[:, :, 1] = 0
    mat[:, :, 2] = 0
    return mat


def ft_grey(mat: np.ndarray) -> np.ndarray:
    """Convert an image to grayscale"""
    grey = np.dot(mat[..., ::-1], [0.299, 0.587, 0.114]).astype(np.uint8)
    return grey
