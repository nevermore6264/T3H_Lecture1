from statistics import median

# init list
int_list = []

# insert element and input value in array
# print array

for i in range(10):
    number = int(input("Enter a number: \n"))
    int_list.insert(i, number)
    i += 1

print("Init list: ")
print(int_list)
print("----------------------------------------")

# sort array use function of python
int_list.sort(reverse=True)
print("Sorted list: ")
print(int_list)
print("----------------------------------------")

# find max element in array
max_element = max(int_list)
print("Max element in array: ")
print(max_element)
print("----------------------------------------")


# find max element in array use custom function
def find_max_value_in_array(list):
    max_e = list[0]
    for i in range(len(list)):
        if max_e <= list[i]:
            max_e = list[i]
        i += 1
    return max_e


print("Max element in array use custom function: ")
print(find_max_value_in_array(int_list))
print("----------------------------------------")

# find min element in array
min_element = min(int_list)
print("Min element in array: ")
print(min_element)
print("----------------------------------------")


# find min element in array use custom function
def find_min_value_in_array(list):
    min_e = list[0]
    for i in range(len(list)):
        if min_e >= list[i]:
            min_e = list[i]
        i += 1
    return min_e


print("Min element in array use custom function: ")
print(find_min_value_in_array(int_list))
print("----------------------------------------")


# find median element in array
def median_list(list):
    sum_list = 0
    for i in range(len(list)):
        sum_list += list[i]
        median_element = sum_list / len(list)
        i += 1
    return median_element


print("Median element in array:")
print(median_list(int_list))
print("----------------------------------------")


# find value elements are odd numbers
def find_odd_number_list(list):
    odd_number_list = []
    for i in range(len(list)):
        if list[i] % 2 != 0:
            odd_number_list.append(list[i])
        i += 1
    return odd_number_list


print("Odd number array:")
print(find_odd_number_list(int_list))
print("----------------------------------------")
