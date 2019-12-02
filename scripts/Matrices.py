def det(mat):
    det_ = 0
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
   
    for m,n in zip(mat[0], range(len(mat[0]))):
        det_ += (-1)**n * m * det(delregion(mat, 0, n))
    return det_


def delregion(mat, m, n):
    if len(mat[0]) == 1:
        return [[1]]
    mat_ = list(list(o) for o in mat)
    mat_.pop(m)
    for row in mat_:
        row.pop(n)
    return mat_


def minverse(mat):
    det_ = det(mat)
    if det_ == 0:
        return
    mat_ = list(list(o) for o in mat)
    for m in range(len(mat)):
        for n in range(len(mat[0])):
            mat_[m][n] = (-1)**(n) * (-1)**(m) * det(delregion(mat, m, n)) / det_
    return t(mat_)
    
            
def t(mat):
    mat_ = list(list(o) for o in mat)
    for m in range(len(mat)):
        for n in range(len(mat[0])):
            mat_[m][n] = mat[n][m]
    return mat_


def mmult(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        mat3 = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for m in range(len(mat3)):
            for n in range(len(mat3[0])):
                for o in range(len(mat2)):
                    mat3[m][n] += mat1[m][o] * mat2[o][n]
        return mat3
