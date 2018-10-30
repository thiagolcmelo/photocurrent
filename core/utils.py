########################################################################
# Useful functions for performing mathmatical calculations             #
# author: Thiago Melo                                                  #
# creation: 2018-10-30                                                 #
# update: 2018-10-30                                                   #

import numpy as np

def solve_eigenproblem(H):
    """
    Find the eigenvalues and eigenvectors for the matrix H

    Params
    ------
    H : matrix
        It is expected to be a N x N numpy.complex128 matrix
    
    Return
    ------
    (values, vectors) tuple with eigenvalues and eigenvectors
    """
    values, vectors = np.linalg.eig(H)
    idx = np.real(values).argsort()
    return values[idx], vectors.T[idx]