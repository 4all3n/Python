# Q)Write a python program using numpy module. Create an array and check the following:
# 1.Type of array
# 2.Shape of the array
# 3.Type of elements in the array
# 4.Size of the array

import numpy as np
#craete an array
array = np.array([[1,2,3],[4,5,6]])

#1.Type of array
arrayType = type(array)
print("Type of Array: ",arrayType)

#2.Shape of the array
arrayShape = array.shape
print("Shape of the Array: ",arrayShape)

#3.Type of elements in the array
arrayTypeElements = array.dtype
print("Type of Elements in the Array: ",arrayTypeElements)

#4.Size of the array
arraySize = array.size
print("Size of the Array: ",arraySize)
