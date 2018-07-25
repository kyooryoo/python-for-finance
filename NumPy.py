import numpy as np

# 1. Array

my_list = [1,3,5,7]
my_list
np.array(my_list)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix
np.array(my_matrix)

range(10)
list(range(3,10,2))
np.arange(3,10,2)

np.zeros(3)
np.zeros((5,5))

np.ones(3)
np.ones((5,5))

np.linspace(0,10,3)
np.linspace(0,100,51)

np.eye(5)

np.random.rand(3)
np.random.rand(5,5)

np.random.randn(3)
np.random.randn(5,5)

np.random.randint(0,101,5)

arr = np.arange(24)
arr
arr.reshape(4,6)

rand_arr = np.random.randint(0,101,10)
rand_arr
rand_arr.max()
rand_arr.min()
rand_arr.argmax()
rand_arr.argmin()

# shape is an attribute
arr.shape
arr
arr.reshape(1,24)
arr.reshape(1,24).shape
arr.reshape(1,24).reshape(24,1)
arr.reshape(24,1)

arr.dtype
np.random.randint(0,101,10).dtype
np.random.rand(10).dtype

# 2 Indexing
arr = np.arange(11,22)
# arr = range(11,22)
arr
arr[8]
arr[8:10]

# broadcasting
arr[8:10] = 100
arr

slice_arr = arr[8:10]
slice_arr

# change all values in the array of slice_arr to 101
slice_arr[:] = 101
slice_arr

# confirm the original array also have values changed
arr = np.arange(0,11)
arr
slice_arr = arr[0:6]
slice_arr[:] = 102
arr

# For getting a copy, be explicit
arr = np.arange(0,11)
arr
slice_arr = arr[0:6].copy() # explicitly specify the copy
slice_arr[:] = 102
arr

arr_2d = np.array(([1,2,3],[4,5,6],[7,8,9]))
arr_2d
arr_2d[1]
arr_2d[1,1]
# slice of the left bottom of the matrix
arr_2d[1:,:2]
# slice of the second row of the matrix
arr_2d[1]
arr_2d[1,:]
# slice of the second column of the matrix
arr_2d[:,1]

arr = np.random.randint(0,101,10)
arr
arr > 50
bool_arr = arr > 50
arr[bool_arr]
# in short
arr[arr>50]
x = 30
arr[arr>30]

# array arithmetic operations
arr = np.arange(0,11)
arr
arr + arr
arr - arr
arr * arr
# 0 / 0 = nan
arr / arr
# 1 / 0 = infinity
1 / arr
arr**3

# square root
np.sqrt(arr)
# exponential (e^)
np.exp(arr)
np.max(arr)
np.sin(arr)
np.log(arr)

np.zeros(10)
np.ones(10)
np.ones(10) * 5
np.arange(10,51)
np.arange(10,51,2)
np.arange(0,9).reshape(3,3)
np.eye(3,3)
np.random.rand(1)
np.random.randn(25)
np.arange(0.01,1.01,0.01).reshape(10,10)
np.linspace(0.01,1,100).reshape(10,10)
np.linspace(0,1,20)

mat = np.arange(1,26).reshape(5,5)
mat
mat[2:,1:]
mat[3,4]
mat[:3,1].reshape(3,1)
mat[:3,1:2]
mat[4]
mat[3:]

np.sum(mat)
mat.sum()
np.std(mat)
mat.std()
# get the sum of all the columns
mat.sum(axis=0) # on the y axis
mat.sum(axis=1) # on the x axis

np.random.seed(101)
np.random.rand(1)