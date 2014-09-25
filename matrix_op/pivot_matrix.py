__author__ = 'Allen Woods'
import copy

def find_max_incolunm(M, column):
    """在矩阵M中，找出column列中绝对值最大的元素所在的行"""
    m = len(M)
    max_el = max(range(column, m), key=lambda i: abs(M[i][column]))
    #print(max_el)
    return max_el


def swaprow_mtrx(M, i, j):
    """交换矩阵M的i、j两行"""
    for k in range(len(M)):
        M[i][k], M[j][k] = M[j][k], M[i][k]
    return M


def elimate_col_apmtrx(M, col):
    """在矩阵M中，用非主元减去主元乘以系数的积，
    其中系数等于非主元行中，与主元同一列（column列）的元素除以主元的商"""
    m = len(M)
    op_row = col + 1
    while op_row < m:
            multi_num = M[op_row][0] / M[col][0]
            for j in range(m):
                if j == 0:
                    M[op_row][j] = multi_num
                else:
                    M[op_row][j] -= multi_num * M[col][j]
            #print('temp_matrix' + str(op_row))
            #print(M)
            op_row += 1
    return M


def gen_pmatrix(M, seq):
    """根据[A|p]矩阵中的p向量生成P矩阵"""
    m = len(M)

    p_matrix = [[0] * m for i in range(m)]
    for i in range(m):
        p_matrix[i][i] = 1

    for i in range(len(seq)):
        if i != seq[i]:
            swaprow_mtrx(p_matrix, i, seq[i])
    return p_matrix


def gen_apmatrix(M):
    """对矩阵M进行操作，生成矩阵[A|p]，P"""
    m = len(M)
    ap_matrix = copy.deepcopy(M)
    seq = []
    for i in range(m):
        maxel_num = find_max_incolunm(ap_matrix, i)
        seq.append(maxel_num)
        swaprow_mtrx(ap_matrix, i, maxel_num)
        elimate_col_apmtrx(ap_matrix, i)

    pmatrix = gen_pmatrix(ap_matrix, seq)
    return ap_matrix, pmatrix