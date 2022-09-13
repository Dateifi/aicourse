import random
import string


def random_string_list(length):
    string_list = []
    for _ in range(length):
        string_list.append(''.join(random.choice(string.ascii_letters) for _ in range(10)))
    return string_list


def insertion_sort(string_list):
    for i in range(1, len(string_list)):
        j = i
        while j > 0 and string_list[j - 1] > string_list[j]:
            string_list[j - 1], string_list[j] = string_list[j], string_list[j - 1]
            j -= 1
    return string_list

def merge_sort(string_list):
    if len(string_list) <= 1:
        return string_list
    mid = len(string_list) // 2
    left = merge_sort(string_list[:mid])
    right = merge_sort(string_list[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

list_100 = random_string_list(100)
list_1000 = random_string_list(1000)
list_10000 = random_string_list(10000)

print(merge_sort(list_100))


