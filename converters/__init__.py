import numpy as np

def NumArray2Str(A,SF=4):
    el='%%.%if'%SF
    if type(A)==np.ndarray:
        if len(A.shape)>1:
            return np.array([[el%element for element in line] for line in A])
        else:
            return np.array([el%element for element in A])
    else:
        return np.array([[el%element for element in line] for line in A])
