import random

def mean_difference_root_error(targets, predictions, n, p):
    m = len(targets)
    total_error = 0
    for i in range(m):
        root_target = targets[i] ** (1/n)
        root_prediction = predictions[i] ** (1/n)
        total_error += abs(root_target - root_prediction) ** p
    md_nre = total_error / m
    return md_nre

def main():
    num_samples = input("Nhập số lượng samples (num_samples): ")
    n = input("Nhập giá trị n cho căn bậc n: ")
    
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    if not n.isnumeric():
        print("n must be an integer number")
        return

    num_samples = int(num_samples)
    n = int(n)

    if num_samples <= 0 or n <= 0:
        print("num_samples and n must be positive integers greater than 0")
        return

    predictions = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]

    for i in range(num_samples):
        print(f"sample-{i}: predict = {predictions[i]:.2f}, target = {targets[i]:.2f}")

    p = input("Nhập giá trị p: ")
    try:
        p = float(p)
    except ValueError:
        print("p must be a number")
        return

    md_nre = mean_difference_root_error(targets, predictions, n, p)

    print(f"MD_{n}RE: {md_nre:.2f}")

if __name__ == "__main__":
    main()
