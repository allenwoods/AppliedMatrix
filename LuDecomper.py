__author__ = 'Allen Woods'

from basic_op import matrix_io
from matrix_op import lu_decomposition

print("——————————————————————————LU分解简单实现（ by Python3）————————————————————————————————")
print("——————————————————————————————Allen Woods———————————————————————————————————————————\n")

print("输入一个N维矩阵")
while True:
    square_num = matrix_io.num_input("N = ")
    A = matrix_io.matrix_input(square_num)
    if A != 0:
        break

P, L, U = lu_decomposition.lu_decomp(A)

print("A:")
matrix_io.matrix_print(A)

print("P:")
matrix_io.matrix_print(P)

print("L:")
matrix_io.matrix_print(L)

print("U:")
matrix_io.matrix_print(U)