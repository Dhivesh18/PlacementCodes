# Methid 1
import numpy as np
b=np.array([[6, 8], [1, 9], [2, 4], [4, 7],[2,10]]).flatten()
print(min(b),max(b))

# Method 2
a=[[6, 8], [1, 9], [2, 4], [4, 7],[2,10]]
b=[a[i][j] for i in range(len(a)) for j in range(2)]
print(min(list(set(b))),max(list(set(b))))
