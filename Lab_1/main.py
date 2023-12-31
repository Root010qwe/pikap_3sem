import math
import sys

def get_coefficient(index, prompt):
    while True:
        try:
            print(prompt)
            return float(sys.argv[index])
        except:
            try:
                return float(input())
            except ValueError:
                print("Введите число")

def calculate_roots(A, B, C):
    if A == 0:
        if B == 0:
            if C == 0:
                print("Любое число")
                return
            else:
                print("Нет корней")
                return
        else:
            xx = (-1) * C / B
            if xx < 0:
                print("Нет корней")
                return
            else:
                roots = [math.sqrt(xx), (-1) * math.sqrt(xx)]
    else:
        D = B ** 2 - 4 * A * C
        if D < 0:
            print("Нет корней")
            return
        else:
            x1 = ((-1) * B - math.sqrt(D)) / (2 * A)
            x2 = ((-1) * B + math.sqrt(D)) / (2 * A)
            roots = []
            if x1 >= 0:
                roots.append(math.sqrt(x1))
                roots.append(-math.sqrt(x1))
            if x2 >= 0:
                roots.append(math.sqrt(x2))
                roots.append(-math.sqrt(x2))
    if not roots:
        print("Нет корней")
        return
    unique_roots = list(set(roots))
    for root in unique_roots:
        print(root)

def main():
    A = get_coefficient(1, 'Введите коэффициент A: ')
    B = get_coefficient(2, 'Введите коэффициент B: ')
    C = get_coefficient(3, 'Введите коэффициент C: ')
    calculate_roots(A, B, C)

if __name__ == "__main__":
    main()
