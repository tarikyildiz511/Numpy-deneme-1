import numpy as np

#pythonlistesi 
liste = [1,2,3,4,5,6,7,8,9]
#numpy listesi
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(liste))
print(type(np_array))

multilist = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)

print(multilist)
print(np_multi)