import random
import math


def calculate_mae(targets, predictions):
    n = len(targets)
    mae = sum(abs(y - y_hat) for y, y_hat in zip(targets, predictions)) / n
    return mae


def calculate_mse(targets, predictions):
    n = len(targets)
    mse = sum((y - y_hat) ** 2 for y, y_hat in zip(targets, predictions)) / n
    return mse


def calculate_rmse(targets, predictions):
    mse = calculate_mse(targets, predictions)
    rmse = math.sqrt(mse)
    return rmse


def main():
    num_samples = input("Nhập số lượng samples (num_samples): ")

    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples)

    loss_name = input("Nhập tên loss function (MAE, MSE, RMSE): ")

    predictions = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]

    if loss_name == 'MAE':
        loss = calculate_mae(targets, predictions)
    elif loss_name == 'MSE':
        loss = calculate_mse(targets, predictions)
    elif loss_name == 'RMSE':
        loss = calculate_rmse(targets, predictions)
    else:
        print(f"{loss_name} is not supported")
        return

    print(f"loss name: {loss_name}")
    for i in range(num_samples):
        print(
            f"sample-{i}: predict = {predictions[i]:.2f}, target = {targets[i]:.2f}")
    print(f"loss: {loss:.2f}")


if __name__ == "__main__":
    main()
