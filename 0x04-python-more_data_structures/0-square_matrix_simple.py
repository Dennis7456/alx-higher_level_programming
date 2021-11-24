#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	temp_matrix = []
	for i in matrix:
		temp_matrix.append(list(map(lambda x: x ** 2, i)))
	return temp_matrix
