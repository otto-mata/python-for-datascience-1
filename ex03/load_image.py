import cv2
import numpy as np
import warnings


def ft_load(path: str) -> np.ndarray:
    """Load an image, print its shape and return
    the raw pixel values as an NDArray"""

    def _read_wrapper(path: str) -> cv2.typing.MatLike | None:
        """Wrap cv2.imread for easier warning production."""
        cv_im = cv2.imread(path)
        if cv_im is None:
            warnings.showwarning(
                f"Could not read file at '{path}'. Empty NDArray returned.",
                RuntimeWarning,
                __file__,
                _read_wrapper.__code__.co_firstlineno,
            )
        return cv_im

    cv_im = _read_wrapper(path)
    if cv_im is None:
        return np.array([], np.uint8)
    print("The shape of image is:", cv_im.shape)
    return np.array(cv_im.data, np.uint8)
