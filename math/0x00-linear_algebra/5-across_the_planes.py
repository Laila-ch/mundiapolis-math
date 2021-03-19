import numpy as np

def add_matrices2D(mat1, mat2) : 
    try : 
        mat1 = np.array(mat1)
        mat2 = np.array(mat2)
        mat = mat1+mat2
        mat = mat.tolist()
        return mat
    except :
        return None
    
    
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
