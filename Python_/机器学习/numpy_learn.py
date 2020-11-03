import numpy as np
A = np.arange(12).reshape((3,4))
print(A)
b = np.concatenate((A,A),axis=1)
print(b)
print(np.array_split(A,3,axis=0))