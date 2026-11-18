import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    vectorized=np.array(x)
    denominator=1+np.exp(-vectorized)
    result=1/denominator
    return result
    pass