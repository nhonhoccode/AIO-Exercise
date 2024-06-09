import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)

def main():
    x = input("Nhập giá trị x: ")
    activation_function = input("Nhập tên activation function (sigmoid, relu, elu): ")

    if not is_number(x):
        print("x must be a number")
        return
    
    x = float(x)
    
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f"{activation_function} is not supported")
        return
    
    if activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'elu':
        result = elu(x)
    
    print(f"{activation_function}: f({x}) = {result}")

if __name__ == "__main__":
    main()
