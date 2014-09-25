__author__ = 'Allen Woods'
from fractions import Fraction


def num_input(notice):
    """根据提示notice，输入数字"""
    while True:
        try:
            temp = input(notice + ':')
            eval(temp) is int
            userInput = eval(temp)
            return userInput
        except:
            print("Please Input a number!")


def matrix_input(M, N=0):
    """生成M*N维矩阵，若仅输入一个数字M，则生成M维方阵"""
    if M | N == 1:
        print("N应大于1！")
        return 0
    if N == 0:
        N = M
    matrix_tmp = []
    for i in range(M):
        print("\n第" + str(i + 1) + "行:")
        line_tmp = []
        for j in range(N):
            num_tmp = num_input("\t第" + str(j + 1) + "个数")
            line_tmp.append(num_tmp)
        matrix_tmp.append(line_tmp)
    return matrix_tmp


def matrix_print(matrix):
    """输出矩阵matrix，若元素为整数则格式化输出，否则以分数形式输出"""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == int(matrix[i][j]):
                print("{0:8d}".format(int(matrix[i][j])), end="\t")
            else:
                tmp = Fraction.from_float(matrix[i][j]).limit_denominator()
                print(" " * (7 - len(str(tmp))), end="\t")
                print(tmp, end="\t")
        print("")
    print("")
