import numpy as np

def nmtom(data):

    nm = 22.5 - (2.5 * (np.log10(data)))
    return nm
