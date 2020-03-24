import numpy as np

a = ([2,-1,0,0], [-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2])

b = np.linalg.eig(a)
print(b)
