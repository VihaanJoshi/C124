A = [3, 2, -1, 9, 5]
print(A)
B = [[1, -2, 3], [8, 4, 6], [-6, 5, 3]]
print(B)

#Method to create a 1D array using Numpy
import numpy as np 
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


#Method-2 to create a 2D array using NumPy
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
type(arr_2d)


#Array with elements of different data types
arr_2d_1 = np.array([[1, 2, 3], ['a, 5, true'], [7, 8, 9]])
print(arr_2d_1)
type(arr_2d_1)


#Accessing elements of 2D lists and arrays

#Accessing elements of 1D list or array
print(A)
print(A[1])
print(arr)
print(arr[2])


#accessing elements of 2D array method1
print(arr_2d)
print(arr_2d[1,2])
#accessing elements of 2D array method2
print(arr_2d[0][1])

#To update an element from 2D list/arrays
print(arr_2d)
print('----------------')
# method 1
arr_2d[1,2]=-4
print(arr_2d)
print('----------------')
# method 2
arr_2d[1,2]=8
print(arr_2d)

