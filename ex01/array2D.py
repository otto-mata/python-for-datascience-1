from typing import TypeVar
import numpy as np

_T = TypeVar("_T")


def slice_me(family: list[list[_T]], start: int, end: int) -> list[list[_T]]:
    """Slices a list, keeping only the part between *start* and *end*."""
    try:
        arr = np.array(
            family,
        )
        print(f"My shape is : {arr.shape}")
        arr = arr[start:end]
        print(f"My new shape is : {arr.shape}")
        return arr.tolist()
    except Exception as ex:
        print(f"{ex.__class__.__name__}: {ex}")
    return []
