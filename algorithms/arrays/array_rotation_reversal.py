# Python program for reversal algorithm of array rotation
# Write a function rotate(arr, d, n) that rotates arr[] of size n by d elements.

# Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7
# A = [1, 2] and B = [3, 4, 5, 6, 7]
#
# Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]


def do_job(arr, d):
    arr_a = arr[0:d]
    arr_b = arr[d:]
    left_rotate(arr_a)
    left_rotate(arr_b)
    # arr_a.extend(arr_b)
    # arr = arr_a
    arr = _extend(arr_a, arr_b)
    return left_rotate(arr)


def left_rotate(arr):
    size = len(arr)
    n = size // 2
    for i in range(0, n):
        temp_a = arr[i]
        temp_b = arr[size - 1 - i]
        arr[size - 1 - i] = temp_a
        arr[i] = temp_b
    return arr


def _extend(arr_1, arr_2):
    result_arr = [None] * (len(arr_1) + len(arr_2))
    m = 0
    for i in range(0, len(arr_1)):
        result_arr[m] = arr_1[i]
        m = m + 1
        if i == len(arr_1) - 1:
            for j in range(0, len(arr_2)):
                result_arr[m] = arr_2[j]
                m = m + 1
    return result_arr


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")


_arr = [1, 2, 3, 4, 5, 6, 7]
_d = 2
result = do_job(_arr, _d)
print_array(result)


