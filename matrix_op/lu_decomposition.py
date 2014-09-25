__author__ = 'Allen Woods'
from matrix_op import pivot_matrix

def lu_decomp(A):
    """对矩阵A做LU分解，生成P，L，U矩阵"""
    n = len(A)

    # Create zero matrices for L, U and AP
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]
    # Create the pivot matrix P and the multipled matrix PA
    AP, P = pivot_matrix.gen_apmatrix(A)

    for row in range(n):
        for col in range(row+1):
            if row == col:
                L[row][col] = 1
            else:
                L[row][col] = AP[row][col]

    for row in range(n):
        for col in range(n - row):
            U[row][n - col - 1] = AP[row][n - col - 1]

    return P, L, U




