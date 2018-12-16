import math


# input: integer number
# output: list have square of the value


def show_the_square_of_the_value(n):
    result_list = []
    for i in range(1, n):
        result_list.append(int(math.pow(i, 2)))
    return result_list


print("Enter a number:")
while True:
    try:
        number = int(input())
        if number >= 1:
            print("List has the square of the value:")
            print(show_the_square_of_the_value(number))
        else:
            print("Number needs > 0")
    except:
        print("Input invalid.Please enter a number again:")
