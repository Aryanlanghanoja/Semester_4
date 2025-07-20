import numpy as np


def correlation_coefficient(x, y):
    """
    Calculate the correlation coefficient between two arrays x and y.

    Args:
        x (array-like): The first array.
        y (array-like): The second array.

    Returns:
        float: The correlation coefficient between x and y.
    """
    # Calculate the correlation coefficient matrix
    correlation_matrix = np.corrcoef(x, y)

    # Return the correlation coefficient value
    return correlation_matrix[0, 1]


# Example usage
x = [1, 2, 3, 4, 5 , 6 , 7, 8, 9]
y = [1, 2, 3, 4, 5 , 6 , 7, 8, 9]

corr_coefficient = correlation_coefficient(x, y)
print("Correlation Coefficient:", corr_coefficient)
