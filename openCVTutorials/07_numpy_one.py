import numpy as np

# create numpy one-d array

arr_oneD = np.array([1, 2, 3])
print(f"Array shape:{arr_oneD.shape} \n dimension: {arr_oneD.ndim} \n OUTPUT: {arr_oneD}")
print()
print()

# Create numpy two_d array
arr_twoD = np.array([[1], [2], [3]])
print(f"Array shape:{arr_twoD.shape} \n Array dimension: {arr_twoD.ndim} \n arr_twoD: {arr_twoD}")
print()
print()

# Create numpy two-d array
arr_2D = np.array([(1, 2, 3), (4, 5, 6)])
print(f"Array shape:{arr_2D.shape} \n Array dimension: {arr_2D.ndim} \n OUTPUT: {arr_2D}")
print()
print()

# Create numpy three-d array
arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"Array shape:{arr_3D.shape} \n Array dimension: {arr_3D.ndim} \n OUTPUT: {arr_3D}")
print()
print()

# Create numpy zeroes array
arr_zeros = np.zeros((3, 3), dtype=np.float32)
print(f"Array shape:{arr_zeros.shape} \n Array dimension: {arr_zeros.ndim} \n OUTPUT: {arr_zeros}")
print()
print()

# Create numpy ones array
arr_ones = np.ones((3, 3), dtype=np.int8)
print(f"Array shape:{arr_ones.shape} \n Array dimension: {arr_ones.ndim} \n OUTPUT: {arr_ones}")
print()
print()

# Create a numpy array with a specific number:
arr_full = np.full((3, 5), 5, dtype="uint")
print(f"Array dimension: {arr_full.ndim} \n OUTPUT: {arr_full}")
print()
print()

# Create identity matrix-
arr_identity = np.eye(3, dtype="int8")
print(f"Array dimension: {arr_identity.ndim} \n OUTPUT: {arr_identity}")
print()
print()

# Create a array with a specific range with a fix interval
# (include,exclude,interval)
arr_fix_interval = np.arange(0, 10, 2)
print(f"Array dimension: {arr_fix_interval.ndim} \n OUTPUT: {arr_fix_interval}")
print()
print()

# Create a array with a specific range and number of element
arr_fix_range = np.linspace(0, 10, 10, dtype="float32")
print(f"Array Dimension: {arr_fix_range.ndim} \n OUTPUT: {arr_fix_range}")
print()
print()

# ______________________________ Create random array ______________________________

arr_random = np.random.randn(2, 4) * 10
print(f"arr_random: {arr_random}")
print()
print()

arr_random_int = np.random.randint(5, size=(3, 3))
print(f"arr_random_int: {arr_random_int}")
print()
print()

# __________________ Total element number ___________________
arr_test = np.array([12.3, 4, 5, 6])
print(f"Total element of: {arr_test} arr_random_int : {arr_test.size}")
print()
print()

# __________________ Datatype element number ___________________
print(f"Data type of:  {arr_test} : {arr_test.dtype}")
print()
print()

# __________________ Change the Dtype of an existing array element  ___________________
arr_one_test = arr_test.astype(dtype=np.int8)
print(f"Data type of:  {arr_one_test} : {arr_one_test.dtype}")
print()
print()

# __________________ Change the Dtype of an existing array element  ___________________
print(f"Minimum:  {arr_one_test.min()} \n maximum: {arr_one_test.max()}")
print()
print()

