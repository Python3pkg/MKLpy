import numpy as np
import random
#from kernels import HPK_kernel as HPK
from sklearn.metrics.pairwise import polynomial_kernel, linear_kernel
from math import sqrt,floor

def fast_HPK(X,T=None,l=10):
    #!!!ONLY IF X AND T ARE NORMALIZED
    #WARNING: this method is unstable due to the numeric approximation
    # I advise to use the normal generators until this problem is not fixed.
    if T == None:
        T = X
    L = linear_kernel(T,X)
    klist = [np.zeros(L.shape,dtype=np.double)+L]   #[L]
    for d in range(1,l):
        k = klist[-1]*L
        #k = L**(d+1)
        #k = np.multiply(klist[-1],L)
        klist.append(k)
    return np.array(klist)

def fast_linearSFK(X, T=None, l=50, f=None, func='rbf'):
    #This is an experimental method
    #it needs more tests
    
    if f==None:
        f = int(max(2,sqrt(X.shape[1])/2.0))
    
    feature_list = [random.choice(list(range(0,X.shape[1]))) for i in range(f)]
    nonused = [i for i in range(X.shape[1]) if i not in feature_list]
    k = linear_kernel(T[:,feature_list],X[:,feature_list])
    klist = [k]
    for d in range(1,l-1):
        e = random.choice(nonused)
        u = random.choice(feature_list)
        nonused.remove(e)
        feature_list.remove(u)
        nonused.append(u)
        feature_list.append(e)
        L1 = linear_kernel(T[:,[e]],X[:,[e]])
        L2 = linear_kernel(T[:,[u]],X[:,[u]])
        k = klist[d-1] + L1 - L2
        klist.append(k)
    return np.array(klist)
