import numpy as np 

def scalar(l1, l2):

    result = 0
    if len(l1) == len(l2):
        for i in range(len(l1)):
            x = l1[i] * l2[i]
            result += x

    else:
        raise NameError('vectors must have the same length')

    return result

l1, l2 = [1, 2, 3], [3, 0, 7]
print(scalar(l1, l2))

def matrix_prd(mat1, mat2):

    r1, c1 = np.shape(mat1)
    r2, c2 = np.shape(mat2)
    result = np.zeros((r1, c2), dtype=int)
    if c1 == r2:
        for i in range(r1):
            row1 = mat1[i]
            for j in range(c2):
                clm1 = [row[j] for row in mat2]

                result[i, j] = scalar(row1, clm1)

        return result

    else:
        raise NameError('Matrix product is possible only between matrices n,m x m,p')

m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[4,2,7],[0,5,0],[1,2,4]])
print(matrix_prd(m1, m2))