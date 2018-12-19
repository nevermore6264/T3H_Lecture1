import math


def check_number(n):
        if n >= 0:
            return int(math.pow(n, 3))
        else:
            return int(math.fabs(n))


while True:
    try:
        print("Enter a number:")
        number = int(input())
        print("Result of check number function :")
        print(check_number(number))
    except:
        print("This is not number")


