# Question 1
import numpy as np

arr = np.arange(0, 10, 1)
print("1A.", arr, sep="\n")

# Question 2
arr = np.ones((3, 3)) > 0
arr1 = np.ones((3, 3), dtype=bool)
arr2 = np.full((3, 3), fill_value=True, dtype=bool)
print("2D.", arr, arr1, arr2, sep="\n")

# Question 3
arr = np.arange(0, 10)
print("3A.", arr[arr % 2 == 1], sep="\n")

# Question 4
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print("4B.", arr, sep="\n")

# Question 5
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print("5B.", arr_2d, sep="\n")

# Question 6
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print("6A.", c, sep="\n")

# Question 7
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("7C.", c, sep="\n")

# Question 8
arr = np.array([1, 2, 3])
print("8A.")
print(np.repeat(arr, 3))
print(np.tile(arr, 3))

# Question 9
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero((a >= 5) & (a <= 10))
print("9C.", a[index], sep="\n")


# Question 10
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print("10D.", pair_max(a, b), sep="\n")

# Question 11
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("11A.", np.where(a < b, b, a), sep="\n")

