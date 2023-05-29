import numpy as np

"""
Description:
    Used for numerical computing.  It provides an array object,
    mathematical functions, and tools for working with large,
    multi-dimensional arrays and matrices.
"""


class Basics:
    # Numpy Arrays: 'ndarray'(n dimensional array)
    def arrayCreationMethods():
        np.array()  # pass and iterable object(i.e. a list) to create an array.
        np.zeros()  # creates arrays with the associated value in name.
        np.ones([5, 5])  # Creates 5 x 5 2D array of ones.
        np.empty()
        np.arange()  # Create array with regularly spaced values.

    def arrayOperations():
        # These operations work without explicit loops.
        x = np.array([1, 2, 3])
        # arithmetic operations
        x_sum = x + 2  # [3, 4, 5]
        x_product = x * 3

        # math
        x_exp = np.exp(x)
        x_sqrt = np.sqrt(x)

        # Statistics
        mean = np.mean(x)
        std = np.std(x)
        max = np.max(x)
        min = np.min(x)

    def indexingAndSlicing():
        # Indexing starts at 0, negative indexing can pull from end of array.
        # Slicing pulls portions of the array.

        x = np.zeros([5, 5])
        x = x[1:4]

    def shaping():
        x = np.zeros([5, 5])
        # x[2][3] = 1 # Note, this would cuase reshape to fail because it can't maintain all the data.
        x.reshape([3, 3])
        # or, same as
        x.reshape(3, 3)

    def broadcasting():
        # Broadcasting is ability to perform operations between arrays of different shapes.
        x = np.ones([2, 2])
        y = np.zeroes([5, 5])

    def universalFunctions():
        # 'ufuncs', operate element-wise on arrays.
        # Optimized for speed and can be appplied to arrays of any size or shape.
        x = np.array([[1, 2, 3], [1, 2, 3]])
        sqr = np.square(x)
        sin = np.sin(x)
        sum = np.sum(x)

    def linearAlgebra():
        # Includes functinos for linear algrebra
        # matrix multiplication, determinant calculation, eigenvalue computation, and more.
        pass
