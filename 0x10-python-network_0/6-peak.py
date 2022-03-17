#!/usr/bin/python3
""" 
Function that finds a peak in a
list of unsorted integers 
"""
	
def find_peak(A):
    """find pick element"""
    if A == []:
        return None

    def recursive(A, left=0, right=len(A) - 1):
        """helper recursive function"""

        mid = (left + right) // 2

        # check if the middle element is greater than its neighbors
        if ((mid == 0 or A[mid - 1] <= A[mid]) and
                (mid == len(A) - 1 or A[mid + 1] <= A[mid])):
            return A[mid]

        # If the left neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the left sublist
        if mid - 1 >= 0 and A[mid - 1] > A[mid]:
            return recursive(A, left, mid - 1)

        # If the right neighbor of `mid` is greater than the middle element,
        # find the peak recursively in the right sublist
        return recursive(A, mid + 1, right)

    return recursive(A)
	
