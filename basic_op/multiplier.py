__author__ = 'Allen Woods'

def mult_matrix(M, N):
    """将两个矩阵相乘"""
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*N)] for a in M]