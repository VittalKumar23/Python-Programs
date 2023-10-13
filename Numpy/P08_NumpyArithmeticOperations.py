import numpy as np

firstArray = np.arange(12).reshape(3, 4)
print("firstArray:")
print(firstArray)

secondArray = np.arange(4)
print("secondArray:")
print(secondArray)

# Adding above two arrays element-wise (NOTE: array shapes should be compatible)
# You can use np.newaxis or reshape to make them compatible
print("Addition:")
print(np.add(firstArray, secondArray[:, np.newaxis]))

# Subtracting above two arrays element-wise
print("Subtraction:")
print(np.subtract(firstArray, secondArray[:, np.newaxis]))

# Multiplying above two arrays element-wise
print("Multiplication:")
print(np.multiply(firstArray, secondArray[:, np.newaxis]))

# Dividing the above two arrays element-wise
# Avoid division by zero, so add 1e-10 to secondArray
print("Division:")
print(np.divide(firstArray, secondArray[:, np.newaxis] + 1e-10))

# numpy.power(): returns array element raised to the specified value
array = np.array([1, 2, 3])
print("Power:")
print(np.power(array, 2))  # [1 4 9]

# Author: OMKAR PATHAK

'''import numpy as np

firstArray = np.arange(12).reshape(3, 4)
print(firstArray)

secondArray = np.arange(4)
print(secondArray)

# adding above two arrays (NOTE: array shapes should be same)
print(np.add(firstArray, secondArray))

# subtracting above two arrays
print(np.subtract(firstArray, secondArray))

# multiplying above two arrays
print(np.multiply(firstArray, secondArray))

# dividing the above two arrays
print(np.divide(firstArray, secondArray))

# numpy.power(): returns array element raised to the specified value result
array = np.array([1, 2, 3])
print(np.power(array, 2))       # [1 4 9]'''



