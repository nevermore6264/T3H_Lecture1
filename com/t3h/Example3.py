import math


# input: integer number
# output: list have square of the value


def show_the_square_of_the_value(number):
        result_list = []
        if number <= 0:
            return "Number needs > 0"

        for i in range(1, number):
            result_list.append(int(math.pow(i, 2)))
        return "List has the square of the value: " +str(result_list)

print("Enter a number:")
while True:
    try:
        number = int(input())
        print(show_the_square_of_the_value(number))
    except:
        print("Input invalid.Please enter a number again:")
