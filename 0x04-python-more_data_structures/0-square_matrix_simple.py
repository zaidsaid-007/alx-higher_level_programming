#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values using nested list comprehension
    return [[element ** 2 for element in row] for row in matrix]
