import math
if __name__ == '__main__':
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    result = sorted(data, key=abs)
    print(result)

    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    result_with_lambda = sorted(data, key=lambda x: math.sqrt(x**2))
    print(result_with_lambda)
