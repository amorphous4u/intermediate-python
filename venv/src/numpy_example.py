__author__='Amit Verma'

from numpy import *

# my_matrix = arange(20).reshape(5,4)
# print(my_matrix)

# array_one = array([1, 3])
# array_two = array([11, 111, 4])
# array_three = array([8, 4, 3])
# print(concatenate((array_one, array_two, array_three)))


array_one = random.randn(5,5)
array_two = random.randn(5,5)
matrix_one = mat(array_one)
matrix_two = mat(array_two)

multipled_matrix = matrix_one.T * matrix_two.I
print(multipled_matrix)