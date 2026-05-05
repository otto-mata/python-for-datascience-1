import sys

import cv2
import numpy as np
from load_image import ft_load


def main(argc: int, argv: list[str]) -> int:
    """Crop and rotate animal.jpeg, then display it."""
    try:
        im = ft_load("animal.jpeg")
        assert im.ndim == 3, "incorrect data dimensions"
        im = np.rot90(im[110:510, 450:850])
        print("After transposing:", im.shape)
        cv2.imshow("Test", im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as ex:
        print(f"{ex.__class__.__name__}: {ex}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main(len(sys.argv), sys.argv))
