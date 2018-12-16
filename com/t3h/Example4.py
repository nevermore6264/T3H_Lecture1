import math

print("Enter a number:")
try:
    number = int(input())
    if number < 0:
        print(int(math.fabs(number)))
    elif number == 0:
        print(number)
    else:
        print(int(math.pow(number, 3)))
except:
    print("This is not number")
