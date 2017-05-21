"""
.. codeauthor:: Ivano Lauriola <ivanolauriola@gmail.com>

================
Input validation
================

.. currentmodule:: MKLpy.utils.validation

This sub-package contains tool to check the input of a MKL algorithm.

"""
from scipy.sparse import issparse
from sklearn.utils import check_array
from cvxopt import matrix
import numpy as np
import types
 
 
def check_KL_Y(K,Y):
    """check if the input is a valid kernel list compliant with MKLpy MKL algorithms.

    Parameters
    ----------
    K : (l,n,m) array_like,
             where *l* is the number of kernels in list and *(n,m)* is the shape of kernels.

    Returns
    -------
    K_ : (l,n,m) ndarray or kernel_list.

    Notes
    -----
    The evaluation is not exaustive due to complexity of a regular list of kernels.
    """
    #TODO
    if not hasattr(K,'__len__'):
        raise TypeError("list of kernels must be array-like")
    
    if type(K) == list:
        K = np.array(K)
    elif K.__class__.__name__ == 'kernel_list':
        K = K
    elif type(K) != np.array:
        K = np.array(list(K))

    #return X

    if len(K.shape) == 2:
        raise TypeError("Expected a list of kernels, found a matrix")
    if len(K.shape) != 3:
        raise TypeError("Expected a list of kernels, found unknown")
    a = K[0]
    check_array(a, accept_sparse='csr', dtype=np.float64, order="C")
    
    if a.shape != (K.shape[1],K.shape[2]):
        raise TypeError("Incompatible dimensions")
    '''
    if X[0].shape[1] != X.shape[1]:
        print X[0].shape,' ',X.shape
        raise TypeError("Incompatible dimensions")
    if len(X) > 1 and X[0].shape != X[1].shape:
        raise TypeError("Incompatible dimensions")
    '''
    return K


def check_squared(K):
    if K.shape[0] != K.shape[1]:
        raise ValueError("K must be squared; shape obtained: "+str(K.shape))
    return K.todense() if issparse(K) else K


def check_K_Y(K,Y):
    K = check_squared(K)
    if len(Y) != K.shape[0]:
        raise ValueError("K and Y have different length")
    return K,np.array(Y)

def check_X_T(X,T):
    T = X if type(T) == type(None) else T
    if X.shape[1] != T.shape[1]:
        raise ValueError("X and T have different features")
    return X,T



def check_cv(cv,Y):
    '''cv e' una lista di split'''
    #TODO
    pass


def check_scoring(estimator, scoring):
    #TODO
    return scoring

