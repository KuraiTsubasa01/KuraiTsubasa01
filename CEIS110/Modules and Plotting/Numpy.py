#The numpy package provides tools for scientific and mathematical computations in Python.
#Numpy uses an array data type that is conceptually similar to a list, consisting of an
#ordered set of elements of the same type.

#Creating arrays
import numpy as np

# 1-dimension array
my_array1 = np.array([15.5, 25.11, 19.0])
print('my_array_1:')
print(my_array1)
print()

# 2-dimension array
my_array2 = np.array([(34, 25), (16, 12)])
print('my_array_2:')
print(my_array2)

#Pre-initialized arrays
import numpy as np

zero_array = np.zeros((1, 5))   # Single dimension array with 5 elements
print('zero_array:')
print(zero_array)
print()

one_array = np.ones((5, 2))  # 5-dimension array with 2 elements in each dimension.
print('one_array:')
print(one_array)


#Creating sequences using linspace().
import numpy as np

print(np.linspace(0, 1, 11))
print()
print(np.linspace(0, np.sin(np.pi/4), 20))


#Array operations program.
import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

print('Adding arrays (array1 + array2)')
print(array1 + array2)
#Adding arrays (array1 + array2)
#[11 22 33 44]

print('\nSubtracting arrays (array1 - array2)')
print(array1 - array2)
#Subtracting arrays (array1 - array2)
#[ 9 18 27 36]

print('\nMultiplying arrays (array1 * array2)')
print(array1 * array2)
#Multiplying arrays (array1 * array2)
#[ 10  40  90 160]

print('\nMatrix multiply (dot(array1 * array2))')
print(np.dot(array1, array2))
#Matrix multiply (dot(array1 * array2))
#300

print('\nFinding square root of each element in array1')
print(np.sqrt(array1))
#Finding square root of each element in array1
#[ 3.16227766  4.47213595  5.47722558  6.32455532]

print('\nFinding minimum element in array1')
print(array1.min())
#Finding minimum element in array1
#10

print('\nFinding maximum element in array1')
print(array1.max())
#Finding maximum element in array1
#40