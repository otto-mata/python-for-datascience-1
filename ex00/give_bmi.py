import numpy as np
import warnings


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[float]:
    """Compute the BMI for every entries.

    In the event of invalid arguments, an empty list is returned and
    warnings are issued.
    """
    try:
        return (np.array(weight) / (np.array(height) ** 2)).tolist()
    except ValueError as ex:
        assert ex.__traceback__
        warnings.showwarning(
            "The arrays need to have the same number of elements",
            RuntimeWarning,
            __file__,
            ex.__traceback__.tb_lineno,
        )
    except TypeError as ex:
        assert ex.__traceback__
        warnings.showwarning(
            "The arrays may only contain integers or floats",
            RuntimeWarning,
            __file__,
            ex.__traceback__.tb_lineno,
        )
    return []


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """Create a list where each entry corresponds to the boolean comparison
    ***E*** < *limit*, for ***E*** each element of the *bmi* argument.

    The "mapping" is done using a numpy vectorized pyfunc.
    """

    def vf(x: float) -> bool:
        return x > limit

    return np.vectorize(vf)(bmi).tolist()
