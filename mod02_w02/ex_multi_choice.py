import numpy as np


# Q1
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length([vector])
print("1D.", round(result, 2))


# Q2
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print("2B.", round(result, 2))

# Q3
x = np.array([[1, 2], [3, 4]])
k = np.array([1, 2])
print("3A.", x.dot(k))

# Q4
x = np.array([[-1, 2], [3, -4]])
k = np.array([1, 2])
print("4B.", x @ k)


# Q5
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print("5A.", result)


# Q6
def matrix_multi_matrix(matrix1, matrix2):
    result = np.matmul(matrix1, matrix2)
    return result


m1 = np.array([[0, 1, 2], [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print("6C.", result)

# Q7
m1 = np.eye(3)
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print("7A.", result)

# Q8
m1 = np.eye(2)
m1 = np.reshape(m1, (-1, 4))[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print("8D.", result)

# Q9
m1 = np.array([[1, 2], [3, 4]])
m1 = np.reshape(m1, (-1, 4), "F")[0]
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print("9B.", result)


# Q10
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print("10A.", result)


# Q11
def compute_eigenvalue_eigenvector(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalue_eigenvector(matrix)
print("11A.", eigenvectors)


# Q12
def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    cos_sim = dot_product / (norm_v1 * norm_v2)
    return cos_sim


x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
result = compute_cosine(x, y)
print("12C.", round((result), 3))