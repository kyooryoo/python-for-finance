import numpy as np

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



