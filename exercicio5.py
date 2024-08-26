# Kata
# Write a function that doubles every second integer in a list, starting from the left.
# Example:
# For input array/list:
# [1, 2, 3, 4]
# the function should return:
# [1, 4, 3 ,8]


def double_every_other(lst):
    count = 1
    for number in lst[1::2]:
        new_number = number * 2
        lst[count] = new_number
        count += 2
    return lst


print(double_every_other([1, 2, 3, 4, 5]))
print(double_every_other([1, 19, 6, 2, 12, -3]))
print(double_every_other([-1000, 1653, 210, 0, 1]))
