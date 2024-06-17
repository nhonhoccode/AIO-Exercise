def factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result


def taylor_sin(x, n):
    sin_approx = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sin_approx += term
    return sin_approx


def taylor_cos(x, n):
    cos_approx = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cos_approx += term
    return cos_approx


def taylor_sinh(x, n):
    sinh_approx = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sinh_approx += term
    return sinh_approx


def taylor_cosh(x, n):
    cosh_approx = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        cosh_approx += term
    return cosh_approx


if __name__ == "__main__":
    x = float(input("Nhập giá trị x (radian): "))
    n = int(input("Nhập số lần lặp muốn xấp xỉ (n): "))

    if n <= 0:
        print("n must be a positive integer greater than 0")
    else:
        print(f"sin({x}) ≈ {taylor_sin(x, n)}")
        print(f"cos({x}) ≈ {taylor_cos(x, n)}")
        print(f"sinh({x}) ≈ {taylor_sinh(x, n)}")
        print(f"cosh({x}) ≈ {taylor_cosh(x, n)}")
