def max_kernel(num_list, k):
    res = []
    for i in range(len(num_list)-k+1):
        res.append(max(num_list[i: i+k]))
    return res


if __name__ == "__main__":
    num_list = [-7, 4, 5, 1, -48, 5, 10, 18, 3100, 1]
    k = 3
    print(max_kernel(num_list, k))
