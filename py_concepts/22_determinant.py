# Calculates the determinant of any square matrix
# by using recursion / cofactor expansion on first row.

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        total = 0
        for i, j in enumerate(matrix[0]):
            minor = [row[:i] + row[i+1:] for row in matrix[1:]]
            total += j * determinant(minor) * ((-1) ** i)
        return total