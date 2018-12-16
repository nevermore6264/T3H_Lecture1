import math


def solve_the_equation(a, b, c):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1= %3.2f và x2= %3.2f " % (x1, x2))
    elif delta == 0:
        print("Phương trình có 1 nghiệm kép x1=x2= %3.2f" % (-b / 2 * a))
    else:
        print("Phương trình vô nghiệm")


a = float(input('Nhập hệ số a: \n'))
b = float(input('Nhập hệ số b: \n'))
c = float(input('Nhập hệ số c: \n'))

print("Kết quả:")
solve_the_equation(a, b, c)
