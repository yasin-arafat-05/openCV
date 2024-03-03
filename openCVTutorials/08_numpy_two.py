import numpy as np

# Numpy Array indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])

arr = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(arr[1][2])

# print column wize data
print(arr[:, 0])
print(arr[:, 1])
print()
print()

# print row wize data
print(arr[1, :])
print(arr[1, 2:4])
print()
print()

# print in reverse order
print(arr[:: -1])
print()
print()

# reshape()
arr_reshape = arr.reshape((1, 8))
print(arr_reshape)
print(arr_reshape.ndim)

# append parameter:
arr_append = np.append(arr_reshape, [10, 30])
print(arr_append)
print()
print()

# delete a element (arr,index)
arr_delete = np.delete(arr_append, 9)
print(arr_delete)
print()
print()

# ravel a array:
arr_ravel = arr_delete.reshape((3, 3))
arr_ravel2 = np.ravel(arr_ravel)  # convert into a vector
print(arr_ravel)
print(arr_ravel2)
print()
print()

# transpose a array:
print(np.transpose(arr_ravel))
print()
print()

