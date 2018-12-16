# find numbers divide 7 equals 0
# number > 2000 and number < 3200
# return a list 


def find_numbers_divide_by_7():
    result_list = []
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            result_list.append(i)
    return result_list


print(find_numbers_divide_by_7())
